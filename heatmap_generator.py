import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Lock random seed and set up our grid setup
# We will simulate 10 target biomarker genes across 6 different patients
np.random.seed(10)
target_genes = [f"TARGET_GENE_{i}" for i in range(1, 11)]
samples = ["Patient_Ctrl_1", "Patient_Ctrl_2", "Patient_Ctrl_3", 
           "Patient_Drug_1", "Patient_Drug_2", "Patient_Drug_3"]

# 2. Fabricate expression values (matrix data)
# Control patients will have low expression (around 2), Drug patients will have high expression (around 7)
ctrl_data = np.random.normal(loc=2, scale=0.5, size=(10, 3))
drug_data = np.random.normal(loc=7, scale=0.8, size=(10, 3))
matrix_data = np.hstack((ctrl_data, drug_data)) # Glue columns side-by-side

# 3. Create the DataFrame spreadsheet grid with row labels (index) and column labels
heatmap_df = pd.DataFrame(matrix_data, index=target_genes, columns=samples)

# 4. Set up the canvas layout
plt.figure(figsize=(10, 6))

# 5. Create the heatmap using a "Cool-to-Warm" color gradient
sns.heatmap(
    data=heatmap_df, 
    cmap="coolwarm", 
    annot=True,         # Automatically prints the exact numerical value inside each box!
    fmt=".2f",          # Rounds the numbers inside the squares to 2 decimal places
    linewidths=0.5,     # Adds a clean white border line between the grid squares
    cbar_kws={'label': 'Expression Level'} # Labels the color bar scale on the right
)

# 6. Customize labels and titles
plt.title("Project 3: Top 10 Target Genes Patient Expression Heatmap", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Patient Cohort Samples", fontsize=12)
plt.ylabel("Target Biomarker Genes", fontsize=12)

# Save the heatmap graphic to your folder
output_image = "expression_heatmap.png"
plt.savefig(output_image, dpi=300, bbox_inches='tight')
print(f"Success! Your heatmap has been generated and saved as '{output_image}'.")