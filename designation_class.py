import pandas as pd

class DesignationClassifier:
    def __init__(self, file_path):
        # Load the dataset and normalize column names
        self.data = pd.read_excel(file_path)
        self.data.columns = self.data.columns.str.strip().str.replace(' ', '_')
    
    def get_classification(self, sector, designation):
        # Normalize the input sector to match normalized column names
        sector = sector.strip().replace(' ', '_')
        
        # Check if the provided sector is in the dataset
        if sector not in self.data.columns:
            return f"Sector '{sector}' not found in the dataset."
        
        # Search for the designation and its rank in the specified sector
        rank_data = self.data[self.data[sector] == designation]
        
        if rank_data.empty:
            return f"Designation '{designation}' not found in sector '{sector}'."
        
        rank = rank_data['Rank'].values[0]
        
        # Determine the class based on the rank
        if 1 <= rank <= 15:
            classification = 'Senior-Level'
        elif 16 <= rank <= 50:
            classification = 'Mid-Level'
        elif 51 <= rank <= 84:
            classification = 'Entry-Level'
        else:
            classification = 'Undefined Rank'
        
        return {
            'Sector': sector.replace('_', ' '),
            'Designation': designation,
            'Rank': rank,
            'Classification': classification
        }

# # File path to the uploaded dataset
# file_path = 'Badge_assignment\desig_rank.xlsx'

# # Initialize the classifier object
# classifier = DesignationClassifier(file_path)

# # Example usage
# sector_input = 'Arts & Entertainment'
# designation_input = 'Editor'

# result = classifier.get_classification(sector_input, designation_input)
# print(result)