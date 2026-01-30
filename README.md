# DBSCAN Customer Behavior Analysis 🚀

This project uses **DBSCAN (Density-Based Spatial Clustering)** to analyze customer behavior
and detect **natural groups and anomalies** (outliers).

A **Flask web application** is built to check whether a new customer/product shows
normal or anomalous behavior based on historical data.

project:-“I built a DBSCAN-based customer behavior analysis project using Python and Flask. The model clusters customers based on purchase patterns without predefining the number of clusters and automatically detects outliers like abnormal or risky behavior. Since DBSCAN doesn’t support direct prediction for new data, I handled this by using distance-based logic to check whether a new customer’s behavior matches existing clusters or is anomalous. I visualized clusters using 2D plots, deployed the app with Flask, and managed the complete project on GitHub.”

Key Insight

DBSCAN does not support prediction for new points.
Instead, distance-based logic is used to check whether a new input is
close to existing dense regions or behaves as an anomaly.

---

## 📌 Why DBSCAN?
- No need to define number of clusters
- Automatically detects outliers
- Ideal for fraud detection & rare behavior analysis

---

## 📊 Features Used
- Age
- Income
- Purchase Frequency
- Purchase Amount
- Satisfaction Score

---

## 🛠 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- DBSCAN
- Flask
- HTML/CSS
