import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

data =pd.read_csv("Week 06/Day 2/PCA-dataset.csv")
print(data.head(10))
print(data.info())
print(data.describe())
print(data.isnull().sum())
print(data.shape)

x = data.drop("target",axis=1)
y = data["target"]
print(x.columns)

#scalling

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
print(x_scaled)

pca = PCA(n_components=2)
x_pca = pca.fit_transform(x_scaled)
print("PCA:")
print(x_pca)
#now checking the shape after applying PCA
print("New shape after Applying PCA:")
print(x_pca.shape)

#now checking the variance
print("Check Variance:")
print(pca.explained_variance_ratio_)

#now calculating the total variance
total_variance = pca.explained_variance_ratio_.sum()
print("Total Variance:")
print(total_variance)

#now coverting PCA into dataframe
pca_data = pd.DataFrame(
    x_pca,
    columns=["PC1","PC2"]

)
print(pca_data)

pca_data["target"] = y.values
print(pca_data)

#now making the graph of pca scatter plot
plt.scatter(
    pca_data["PC1"],
    pca_data["PC2"],
    c=pca_data["target"]
)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA(Wine Dataset)")
plt.savefig(
    "pca_wine_scatter.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

variance = pca.explained_variance_ratio_
plt.bar(
    ["PC1", "PC2"],
    variance
)
plt.xlabel("Principal Components")
plt.ylabel(" Variance Ratio")
plt.title("PCA Variance")
plt.savefig(
    "pca_explained_variance.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()