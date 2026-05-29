import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create our mock dataset of 500 genes
np.random.seed(42)
num_genes = 500
genes = [f"GENE_{i}" for i in range(1, num_genes + 1)]
log2_fc = np.random.normal(loc=0, scale=2, size=num_genes)
p_values = np.random.uniform(low=0.00001, high=1.0, size=num_genes)

gene_records_df = pd.DataFrame({
    'Gene': genes,
    'log2FoldChange': log2_fc,
    'pvalue': p_values
})

# 2. Calculate -log10 p-value
gene_records_df['-log10_pvalue'] = -np.log10(gene_records_df['pvalue'])

# 3. NEW: Group genes by their statistical significance thresholds
# Condition for Upregulated: LFC > 1 AND -log10(p-value) > 1.3
# Condition for Downregulated: LFC < -1 AND -log10(p-value) > 1.3
conditions = [
    (gene_records_df['log2FoldChange'] > 1) & (gene_records_df['-log10_pvalue'] > 1.3),
    (gene_records_df['log2FoldChange'] < -1) & (gene_records_df['-log10_pvalue'] > 1.3)
]
choices = ['Upregulated', 'Downregulated']

# If a gene doesn't meet either condition, label it 'Not Significant'
gene_records_df['Expression'] = np.select(conditions, choices, default='Not Significant')

# 4. Set up the canvas layout
plt.figure(figsize=(8, 6))
sns.set_theme(style="whitegrid")

# Create a custom color map matching our labels
color_map = {
    'Upregulated': '#FF4B4B',      # Bright Red
    'Downregulated': '#1F77B4',    # Bright Blue
    'Not Significant': '#D3D3D3'   # Light Gray
}

# 5. Create the scatter plot using the "hue" setting to apply our colors
sns.scatterplot(
    data=gene_records_df, 
    x='log2FoldChange', 
    y='-log10_pvalue', 
    hue='Expression',       # Color the dots based on the Expression column
    palette=color_map,      # Use our custom color map
    alpha=0.8, 
    edgecolor=None
)

# 6. Add customized labels and titles
plt.title("Project 3: Colored Genomic Volcano Plot", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Log2 Fold Change (LFC)", fontsize=12)
plt.ylabel("-Log10 (p-value)", fontsize=12)

# Add threshold lines
plt.axvline(x=1, color='black', linestyle='--', alpha=0.4)
plt.axvline(x=-1, color='black', linestyle='--', alpha=0.4)
plt.axhline(y=1.3, color='black', linestyle='--', alpha=0.4)

# Move the color legend outside the plot so it doesn't cover data points
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Gene Status')

# Save the final image
output_image = "volcano_plot_colored.png"
plt.savefig(output_image, dpi=300, bbox_inches='tight')
print(f"Success! Your upgraded plot has been saved as '{output_image}'.")