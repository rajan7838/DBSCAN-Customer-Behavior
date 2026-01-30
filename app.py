from flask import Flask, render_template, request
import numpy as np
import pickle
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

df = pd.read_csv('customer_data.csv')
df.head()

df['purchase_frequency'] = df['purchase_frequency'].map({'rare':1,
                                                         'occasional':2,
                                                        'frequent':3})

X = df[["age","income","purchase_frequency","purchase_amount","satisfaction_score"]]

scaler = StandardScaler()
X_scaler = scaler.fit_transform(X)

pickle.dump(scaler,open("scaler.pkl",'wb'))

dbscan = DBSCAN(eps=0.8,min_samples=5)
dbscan.fit(X_scaler)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    user_data = np.array([[ 
        float(request.form["age"]),
        float(request.form["income"]),
        float(request.form["frequency"]),
        float(request.form["amount"]),
        float(request.form["satisfaction"])
    ]])

    user_scaled = scaler.transform(user_data)

    # Distance to nearest point
    distances = np.linalg.norm(X_scaler - user_scaled, axis=1)

    if distances.min() < 0.9:
        result = "Normal Customer Behavior"
    else:
        result = "Anomalous / Risky Customer"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)