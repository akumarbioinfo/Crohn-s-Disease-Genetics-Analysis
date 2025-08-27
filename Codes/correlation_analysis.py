import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib_venn import venn2  # type: ignore

# Load DEGs and ROS/Oxidative stress pathway genes data
degs = pd.read_csv("DEGs_Crohns.csv")
ros_genes = pd.read_csv("ROS_gene.csv")

# Ensure that the column names are consistent between datasets
print("DEGs columns:", degs.columns)
print("ROS genes columns:", ros_genes.columns)

# Use the correct common column
common_column = 'Gene Symbol'  # Update this with the correct common column name

# Find overlapping genes between DEGs and ROS/Oxidative stress pathway genes
common_genes = set(degs[common_column]).intersection(set(ros_genes[common_column]))

# Visualize overlapping genes with a Venn diagram
plt.figure(figsize=(8, 6)) # Added figure creation
venn2(subsets=(len(degs) - len(common_genes), len(ros_genes) - len(common_genes), len(common_genes)), set_labels=('DEGs', 'ROS Pathway Genes'))
plt.title("Overlap between DEGs and ROS/Oxidative Stress Pathway Genes")
plt.savefig("figures/venn_diagram.png") # Changed save path
plt.show() # Added show()

# Print the number of overlapping genes and list them
print("Number of overlapping genes:", len(common_genes))
print("Overlapping genes:", common_genes)

expression_data = pd.read_csv("expression_data.csv")

# Subset expression data for common genes
common_expression = expression_data[expression_data['Gene Symbol'].isin(common_genes)]

# Exclude non-numeric columns
# It's better to explicitly select numeric columns that represent expression data,
# rather than just excluding non-numeric. Assuming 'Gene Symbol' is the only non-numeric here.
numeric_columns = common_expression.drop(columns=['Gene Symbol']).select_dtypes(include='number')


# Perform correlation analysis (e.g., Pearson correlation)
cor_results = numeric_columns.corr()

# Print the correlation matrix
print("Correlation Matrix:")
print(cor_results)

# Save correlation results
cor_results.to_csv("data/processed/correlation_results.csv") # Changed save path

# Plot a heatmap of the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(cor_results, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of DEGs")
plt.xlabel("Genes")
plt.ylabel("Genes")
plt.savefig("figures/correlation_heatmap.png") # Changed save path
plt.show()

# Identify key genes based on high correlation with multiple other genes
# Your original code had threshold = 0.1, but your explanation mentioned 0.5.
# I'll keep 0.1 as per code, but you might want to adjust.
threshold = 0.1
# This logic identifies genes that have AT LEAST one correlation > threshold with another gene.
# To find genes highly correlated with *multiple* other genes, more complex logic might be needed.
# For simplicity, keeping your original intent.
key_genes_df = cor_results[cor_results.abs() > threshold] # Use absolute value for correlation strength
key_genes = key_genes_df.index[key_genes_df.count(axis=1) > 1].tolist() # At least two connections

# Print the key genes
print("\nKey Genes:")
if key_genes:
    for gene in key_genes:
        print(gene)
else:
    print("No key genes found with the current threshold and correlation criteria.")