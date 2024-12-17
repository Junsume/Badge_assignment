import pandas as pd

class OrganizationClassifier:
    def __init__(self, university_file, company_file):
        # Load datasets and normalize column names
        self.university_data = pd.read_excel(university_file)
        self.university_data.columns = self.university_data.columns.str.strip().str.replace(' ', '_').str.lower()

        self.company_data = pd.read_excel(company_file)
        self.company_data.columns = self.company_data.columns.str.strip().str.replace(' ', '_').str.lower()

    def classify_organization(self, org_type, organization):
        # Normalize input organization type
        org_type = org_type.strip().lower()

        # Choose the appropriate dataset
        if org_type == 'university':
            data = self.university_data
            name_column = 'institution_name'
            rank_column = 'rank'
        elif org_type == 'company':
            data = self.company_data
            name_column = 'company'
            rank_column = 'global_rank'
        else:
            return f"Organization type '{org_type}' is invalid. Please choose 'university' or 'company'."

        # Search for the organization and its rank
        rank_data = data[data[name_column].str.contains(organization, case=False, na=False)]

        if rank_data.empty:
            return f"Organization '{organization}' not found in '{org_type}' dataset."

        rank = rank_data[rank_column].values[0]

        # Determine the class based on the rank
        if org_type == 'university':
            if 1 <= rank <= 10:
                classification = 'well-known'
            elif 11 <= rank <= 50:
                classification = 'large'
            elif 51 <= rank <= 100:
                classification = 'medium'
            elif 101 <= rank <= 200:
                classification = 'small'
            else:
                classification = 'non-profit'
        elif org_type == 'company':
            if 1 <= rank <= 20:
                classification = 'well-known'
            elif 21 <= rank <= 100:
                classification = 'large'
            elif 101 <= rank <= 200:
                classification = 'medium'
            elif 201 <= rank <= 500:
                classification = 'small'
            else:
                classification = 'non-profit'

        return {
            'Organization_Type': org_type,
            'Organization_Name': organization,
            'Rank': rank,
            'Classification': classification
        }

# # File paths for the datasets
# university_file = 'Badge_assignment\QSWUR2025.xlsx'
# company_file = 'Badge_assignment\Top2000CompaniesGlobally.xlsx'

# # Initialize the classifier object
# classifier = OrganizationClassifier(university_file, company_file)

# # Example usage
# org_type_input = 'university'
# organization_input = 'Harvard University'

# result = classifier.classify_organization(org_type_input, organization_input)
# print(result)
