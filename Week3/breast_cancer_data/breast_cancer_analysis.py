### Week 3- Activity 3: using parquet  format for big data
 
# - Develop a Python project using an object-oriented (OO) approach to convert large datasets into Parquet format. Then, compute the maximum, minimum, average, and absolute values for each column in the dataset. (see link to download a big numerical data in csv format from link: https://archive.ics.uci.edu/datasets)
# Finally, share the GitHub repository link along with a screenshot of the results.

import pandas as pd
import numpy as np

class BreastCancerDataProcessor:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.data = None
        self.numeric_columns = None
        
    def load_data(self):
        #Load data from CSV file
        print("Loading data from CSV file...")
        self.data = pd.read_csv(self.csv_file_path)

        # Get only numeric columns (exclude Diagnosis)
        self.numeric_columns = self.data.select_dtypes(include=[np.number]).columns

    def convert_to_parquet(self):
        # Check if data is loaded
        if self.data is None:
            print("Load the data first!")
            return

        # Convert do parquet
        print("Converting data to Parquet format...")

        self.data.to_parquet('Week3/breast_cancer_data/breast_cancer_data.parquet', index=False)

        print("Parquet file created: breast_cancer_data.parquet")

    def calculate_statistics(self):
        print("Statistics for each column:")
        
        for column in self.numeric_columns:
            print(f"\n{column.upper()}:")
            col_data = self.data[column]
            
            # Maximum value
            max_val = col_data.max()
            print(f"    Maximum: {max_val}")
            
            # Minimum value
            min_val = col_data.min()
            print(f"    Minimum: {min_val}")
            
            # Average value
            mean_val = col_data.mean()
            print(f"    Mean: {mean_val}")
            
            # Absolute values (first 5 as example)
            abs_values = col_data.abs().head(5).tolist()
            print(f"    First 5 absolute values: {abs_values}")
            
def main():
    # Create processor instance
    processor = BreastCancerDataProcessor('Week3/breast_cancer_data/breast_cancer_data.csv')
    
    # Load data from
    processor.load_data()
    
    # Convert to Parquet
    processor.convert_to_parquet()
    
    # Compute statistics
    processor.calculate_statistics()

if __name__ == "__main__":
    main()