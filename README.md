# AMR Extract and Visualize Script

### Overview
amr_extract_visualize.py is a Python script designed to process AMRFinder Plus output files, extracting antimicrobial resistance (AMR) information and generating visual representations in the form of binary heatmaps. The script allows users to specify Class, Subclass, or Gene symbol as the filter criteria and produces two outputs: an AMR summary and binary presence/absence matrix, along with heatmaps to visualize the data.

### Features
Extract specific AMR information based on user-defined Class, Subclass, or Gene symbol.
Generate two outputs:
AMR Info Summary: Detailed count information.
Binary Presence/Absence Matrix: Visualized as heatmaps.
Produce heatmaps with and without hierarchical clustering.
Automatic adjustment of visual parameters for clarity.
### Example Test Data
Two example files are included in the test/input folder:

CLN001_output
CLN002_output
After running the script, results will be generated in the test/output folder.

### Usage
#### Prerequisites
Make sure you have the following Python libraries installed:

pandas
seaborn
matplotlib

#### Running the Script
Run the following command:

`python amr_extract_visualize.py`

Follow the prompts:
Choose to filter by Class, Subclass, or Gene symbol.
Enter the specific values (separated by commas) for extraction.
The script will create results in the output folder.

Example Command Execution

`python amr_extract_visualize.py`

User Prompts:
Choose a column to filter (Class, Subclass, or Gene symbol): Subclass
Enter the specific Subclass(s) you want to extract (separate multiple values with commas): CARBAPENEM, COLISTIN
The output files will be generated in:

-   **test/output/AMR_info.csv**
-   **test/output/Binary_info.csv**
-   **test/output/heatmap_no_clustering.pdf**
-   **test/output/heatmap_with_clustering.pdf**

### Output Descriptions
AMR_info.csv: Summarizes AMR information by Organism, showing Class, Subclass, Gene symbol, and Count.
Binary_info.csv: Binary presence/absence matrix of Gene symbols for each Organism.
Heatmaps:
heatmap_no_clustering.pdf: Visualizes the binary matrix without clustering.
heatmap_with_clustering.pdf: Visualizes the binary matrix with hierarchical clustering to highlight similarities.

### Example Test Folder Structure
``` test/
├── input/
│   ├── CLN001_output
│   └── CLN002_output
└── output/
    ├── AMR_info.csv
    ├── Binary_info.csv
    ├── heatmap_no_clustering.pdf
    └── heatmap_with_clustering.pdf
``` 
### Citation
If you are using the amr_extract_visualize.py script, please cite it as follows:

Sharma, V. (2024). amr_extract_visualize.py [Python script]. Retrieved from [[(https://github.com/vsmicrogenomics/amr_extract_visualize)](https://github.com/vsmicrogenomics/amr_extract_visualize)]

### Acknowledgements
This script utilizes AMRFinderPlus output for extraction. Please acknowledge the use of AMRFinderPlus by referring to the tool at https://github.com/ncbi/amr
