import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# 1. Load Dataset
data = pd.read_csv("Week 06/Day 1/customers.csv")
# 2. Explore Dataset
print(data.head())
print(data.shape)
print(data.info())
print(data.describe())
print(data.isnull().sum())
# 3. Select Features
X = data[
    [
        "Age",
        "Annual_Income_k",
        "Spending_Score"
    ]
]
# 4. Scale Features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# 5. Elbow Method
inertia = []

for k in range(1, 11):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X_scaled)

    inertia.append(model.inertia_)
# 6. Plot Elbow Curve
plt.plot(
    range(1, 11),
    inertia,
    marker="o"
)
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.savefig("elbow_method.png", dpi=300, bbox_inches="tight")
plt.show()

# 7. Create Final K-Means Model
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)
# 8. Train Model
kmeans.fit(X_scaled)
# 9. Get Cluster Labels
data["Cluster"] = kmeans.labels_
# 10. Display Clustered Data
print(data)
# 11. Get Cluster Centers
centers = scaler.inverse_transform(
    kmeans.cluster_centers_
)
print("Cluster Centers:")
print(centers)
# 12. Visualize Clusters
plt.scatter(
    data["Annual_Income_k"],
    data["Spending_Score"],
    c=data["Cluster"]
)
plt.scatter(
    centers[:, 1],
    centers[:, 2],
    marker="X",
    s=200
)
plt.xlabel("Annual Income (k)")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation using K-Means")
plt.savefig(
    "customer_clusters.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
# 13. Analyze Clusters
cluster_summary = data.groupby("Cluster")[
    [
        "Age",
        "Annual_Income_k",
        "Spending_Score"
    ]
].mean()
print("Cluster Summary:")
print(cluster_summary)