import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

class DataAnalyzer:
    def __init__(self, file_path):
        """Initialize DataAnalyzer with the path to your data file."""
        self.file_path = file_path
        self.df = None
        self.analysis_results = {}
        
    def load_data(self):
        """Load data from CSV or Excel file."""
        try:
            if self.file_path.endswith('.csv'):
                self.df = pd.read_csv(self.file_path)
            elif self.file_path.endswith(('.xlsx', '.xls')):
                self.df = pd.read_excel(self.file_path)
            print(f"Successfully loaded data with {self.df.shape[0]} rows and {self.df.shape[1]} columns")
            return True
        except Exception as e:
            print(f"Error loading file: {str(e)}")
            return False

    def basic_analysis(self):
        """Perform basic analysis on the dataset."""
        if self.df is None:
            return "Please load data first"
        
        self.analysis_results['basic'] = {
            'missing_values': self.df.isnull().sum().to_dict(),
            'descriptive_stats': self.df.describe().to_dict(),
            'data_types': self.df.dtypes.to_dict()
        }
        
    def generate_visualizations(self, output_dir='analysis_outputs'):
        """Generate and save basic visualizations."""
        if self.df is None:
            return "Please load data first"
            
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Numerical columns correlation heatmap
        numerical_cols = self.df.select_dtypes(include=[np.number]).columns
        if len(numerical_cols) > 1:
            plt.figure(figsize=(10, 8))
            sns.heatmap(self.df[numerical_cols].corr(), annot=True, cmap='coolwarm')
            plt.title('Correlation Heatmap')
            plt.tight_layout()
            plt.savefig(f'{output_dir}/correlation_heatmap.png')
            plt.close()
            
        # Distribution plots for numerical columns
        for col in numerical_cols:
            plt.figure(figsize=(8, 6))
            sns.histplot(self.df[col], kde=True)
            plt.title(f'Distribution of {col}')
            plt.tight_layout()
            plt.savefig(f'{output_dir}/distribution_{col}.png')
            plt.close()
            
    def generate_report(self, output_dir='analysis_outputs'):
        """Generate a summary report of the analysis."""
        if self.df is None:
            return "Please load data first"
            
        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_path = f'{output_dir}/analysis_report_{timestamp}.txt'
        
        with open(report_path, 'w') as f:
            f.write("DATA ANALYSIS REPORT\n")
            f.write("=" * 50 + "\n\n")
            
            f.write("1. Dataset Overview\n")
            f.write("-" * 20 + "\n")
            f.write(f"Number of rows: {self.df.shape[0]}\n")
            f.write(f"Number of columns: {self.df.shape[1]}\n\n")
            
            f.write("2. Missing Values Summary\n")
            f.write("-" * 20 + "\n")
            for col, missing in self.analysis_results['basic']['missing_values'].items():
                f.write(f"{col}: {missing} missing values\n")
            f.write("\n")
            
            f.write("3. Statistical Summary\n")
            f.write("-" * 20 + "\n")
            for col in self.df.select_dtypes(include=[np.number]).columns:
                f.write(f"\n{col}:\n")
                stats = {k: v[col] for k, v in self.analysis_results['basic']['descriptive_stats'].items()}
                for stat, value in stats.items():
                    f.write(f"{stat}: {value:.2f}\n")
                    
        return report_path

def main():
    # Example usage
    analyzer = DataAnalyzer('data.csv')
    
    if analyzer.load_data():
        # Perform analysis
        analyzer.basic_analysis()
        analyzer.generate_visualizations()
        report_path = analyzer.generate_report()
        
        print(f"\nAnalysis complete! Report saved to: {report_path}")
        print("Visualizations have been saved to the analysis_outputs directory")

if __name__ == "__main__":
    main()
