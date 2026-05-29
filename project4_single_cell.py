import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# We reach into scikit-learn and grab ONLY the PCA tool
from sklearn.decomposition import PCA

# ---------------------------------------------------------
# STEP 1: Simulate 300 Single Cells across 500 Genes
# ---------------------------------------------------------
np.random.seed(42)

# We will create 3 distinct cell types (e.g., T-Cells, B-Cells, and Tumor Cells)
# Each cell type expresses a different pattern of genes
n_cells_per_type = 100
n_genes = 500

# Cell Type 1: High expression in first 100 genes
type1 = np.random.normal(loc=5.0, scale=1.0, size=(n_cells_per_type, n_genes))
type1[:, 0:100] += 4.0 

# Cell Type 2: High expression in middle 100 genes
type2 = np.random.normal(loc=5.0, scale=1.0, size=(n_cells_per_type, n_genes))
type2[:, 100:200] += 4.0

# Cell Type 3: High expression in trailing 100 genes
type3 = np.random.normal(loc=5.0, scale=1.0, size=(n_cells_per_type, n_genes))
type3[:, 200:300] += 4.0

# Stack them all together into one big matrix (300 cells total, 500 columns/genes)
raw_matrix = np.vstack([type1, type2, type3])

# Create a list of labels so we know which cell is which
cell_labels = (['T-Cell'] * 100) + (['B-Cell'] * 100) + (['Tumor-Cell'] * 100)

print(f"Raw Matrix Shape: {raw_matrix.shape} (Cells, Genes)")

# ---------------------------------------------------------
# STEP 2: The Compactor — Applying PCA
# ---------------------------------------------------------
# We tell the PCA tool: "Take those 500 genes and compress them into 2 columns"
pca_tool = PCA(n_components=2)

# We feed our raw matrix into the tool to calculate and transform the data
compressed_coordinates = pca_tool.fit_transform(raw_matrix)

print(f"Compressed Matrix Shape: {compressed_coordinates.shape} (Cells, Components)")

# ---------------------------------------------------------
# STEP 3: Organize into a Pandas DataFrame for Plotting
# ---------------------------------------------------------
df = pd.DataFrame(compressed_coordinates, columns=['PC1', 'PC2'])
df['Cell_Type'] = cell_labels

# ---------------------------------------------------------
# STEP 4: Visualize the Cell Islands
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='PC1', y='PC2', hue='Cell_Type', palette='Set2', s=60)

plt.title("Project 4: Single-Cell Dimensionality Reduction (PCA)")
plt.xlabel("Principal Component 1 (PC1)")
plt.ylabel("Principal Component 2 (PC2)")
plt.legend(title="Identified Cell Types")
plt.grid(True, linestyle='--', alpha=0.5)

# Save the finished graphic product
plt.savefig("single_cell_clusters.png", dpi=300)
plt.show()