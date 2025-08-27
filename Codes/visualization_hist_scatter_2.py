import pandas as pd
import matplotlib.pyplot as plt

# Read merged data from CSV
merged_df = pd.read_csv('merged_data1.csv')

# Plot histograms of ROS relevance scores, baseMean, and additional factors
plt.figure(figsize=(18, 5))  # Adjust the figure size as needed

# Plot histograms for ROS relevance scores
plt.subplot(1, 3, 1)
plt.hist(merged_df['Relevance score'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('ROS Relevance Score')
plt.ylabel('Frequency')
plt.title('Distribution of ROS Relevance Scores')

# Plot histograms for baseMean
plt.subplot(1, 3, 2)
plt.hist(merged_df['baseMean'], bins=20, color='salmon', edgecolor='black')
plt.xlabel('baseMean')
plt.ylabel('Frequency')
plt.title('Distribution of baseMean')

# Plot histograms for an additional factor (e.g., padj)
plt.subplot(1, 3, 3)
plt.hist(merged_df['padj'], bins=20, color='lightgreen', edgecolor='black')
plt.xlabel('padj')
plt.ylabel('Frequency')
plt.title('Distribution of padj')

plt.tight_layout()
plt.show()

# Plot scatter plots of ROS relevance scores vs. additional factors
plt.figure(figsize=(18, 6))  # Adjust the figure size as needed

# Plot scatter plot of ROS relevance scores vs. baseMean
plt.subplot(1, 2, 1)
plt.scatter(merged_df['Relevance score'], merged_df['baseMean'], color='blue', alpha=0.7)
plt.xlabel('ROS Relevance Score')
plt.ylabel('baseMean')
plt.title('ROS Relevance Score vs. baseMean')
plt.grid(True)

# Plot scatter plot of ROS relevance scores vs. padj
plt.subplot(1, 2, 2)
plt.scatter(merged_df['Relevance score'], merged_df['padj'], color='orange', alpha=0.7)
plt.xlabel('ROS Relevance Score')
plt.ylabel('padj')
plt.title('ROS Relevance Score vs. padj')
plt.grid(True)

plt.tight_layout()
plt.show()