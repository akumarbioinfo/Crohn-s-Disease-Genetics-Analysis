import pandas as pd
import matplotlib.pyplot as plt

# Read merged data from CSV
merged_df = pd.read_csv('merged_data1.csv')

# Plot histograms of ROS relevance scores and log2FoldChange
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(merged_df['Relevance score'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('ROS Relevance Score')
plt.ylabel('Frequency')
plt.title('Distribution of ROS Relevance Scores')

plt.subplot(1, 2, 2)
plt.hist(merged_df['baseMean'], bins=20, color='salmon', edgecolor='black')
plt.xlabel('baseMean')
plt.ylabel('Frequency')
plt.title('Distribution of baseMean')

plt.tight_layout()
plt.show()

# Plot scatter plot of ROS relevance scores vs. log2FoldChange
plt.figure(figsize=(8, 6))
plt.scatter(merged_df['Relevance score'], merged_df['baseMean'], color='green', alpha=0.7)
plt.xlabel('ROS Relevance Score')
plt.ylabel('baseMean')
plt.title('ROS Relevance Score vs. baseMean')
plt.grid(True)
plt.show()