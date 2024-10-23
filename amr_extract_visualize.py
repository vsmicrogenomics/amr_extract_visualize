import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from collections import Counter

# User option to choose column: Class, Subclass, or Gene symbol
column_option = input("Choose a column to filter (Class, Subclass, or Gene symbol): ").strip()
specific_values = input(f"Enter the specific {column_option}(s) you want to extract (separate multiple values with commas): ").strip().split(',')

# Trim any extra whitespace around the values
specific_values = [value.strip() for value in specific_values]

input_dir = "./input/"
output_dir = "./output/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

amr_info = []
binary_data = {}

# Process each file in the input directory
for file in sorted(os.listdir(input_dir)):
    if file.endswith("_output"):
        organism = file.replace("_output", "")
        file_path = os.path.join(input_dir, file)
        
        # Read the file assuming it's tab-delimited
        df = pd.read_csv(file_path, delimiter='\t')
        
        # Filter data based on the chosen column option and specific values
        filtered_data = df[df[column_option].isin(specific_values)]
        
        # Count occurrences of the chosen Subclass/Gene/Class
        subclass_count = Counter(filtered_data["Subclass"])
        
        # Store AMR info
        for subclass, count in subclass_count.items():
            gene_symbols = filtered_data[filtered_data["Subclass"] == subclass]["Gene symbol"].unique()
            for gene in gene_symbols:
                amr_info.append([organism, column_option, subclass, gene, count])
        
        # Create binary presence/absence data
        gene_presence = filtered_data["Gene symbol"].unique()
        binary_data[organism] = {gene: 1 if gene in gene_presence else 0 for gene in gene_presence}

# Create DataFrames for outputs and sort them
amr_info_df = pd.DataFrame(amr_info, columns=["Organism", "Class/Subclass/Gene Symbol", "Subclass", "Gene symbol", "Count"])
amr_info_df = amr_info_df.sort_values(by=["Organism", "Subclass", "Gene symbol"])

binary_df = pd.DataFrame(binary_data).T.fillna(0).astype(int).sort_index()

# Save outputs
amr_info_df.to_csv(os.path.join(output_dir, "AMR_info.csv"), index=False)
binary_df.to_csv(os.path.join(output_dir, "Binary_info.csv"), index=True)

# Adjust font scale based on data size
num_organisms, num_genes = binary_df.shape
font_scale = min(1.0, 20.0 / max(num_organisms, num_genes))

# Define color map: Green for 0 (absence), Red for 1 (presence)
cmap = ListedColormap(["green", "red"])

# Create heatmap without hierarchical clustering and save as PDF
plt.figure(figsize=(10, 8))
sns.set(font_scale=font_scale)
sns.heatmap(binary_df, cmap=cmap, cbar=True, linewidths=.5, cbar_kws={"ticks": [0, 1], "label": "Presence (Red) / Absence (Green)"})
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "heatmap_no_clustering.pdf"), format='pdf')
plt.close()

# Create heatmap with hierarchical clustering and save as PDF
sns.set(font_scale=font_scale)
g = sns.clustermap(binary_df, cmap=cmap, cbar=True, linewidths=.5, cbar_kws={"ticks": [0, 1], "label": "Presence (Red) / Absence (Green)"})
g.ax_heatmap.set_xticklabels(g.ax_heatmap.get_xticklabels(), rotation=90)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "heatmap_with_clustering.pdf"), format='pdf')
plt.close()

print("Processing complete. Check the output folder for results including heatmaps (PDF).")
