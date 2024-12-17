import sys
sys.path.append("Badge_assignment\designation_class.py")
from designation_class import DesignationClassifier
from org_class import OrganizationClassifier

def calculate_score(experience_years, education_degrees, serving_org_type, designation, 
                    previous_engagement, audience, demographics, honors_awards, publications):
    # Scoring based on the provided criteria
    experience_score = 0
    if experience_years <= 2:
        experience_score = 0
    elif experience_years <= 5:
        experience_score = 5
    elif experience_years <= 10:
        experience_score = 10
    else:
        experience_score = 15

    education_score = 0
    if education_degrees == 0:
        education_score = 0
    elif education_degrees == 1:
        education_score = 5
    elif education_degrees == 2:
        education_score = 10
    else:
        education_score = 15

    serving_org_score = {
        'non-profit': 5,
        'small': 10,
        'medium': 15,
        'large': 20,
        'well-known': 25
    }.get(serving_org_type.lower(), 0)

    designation_score = {
        'entry-level': 0,
        'mid-level': 5,
        'senior-level': 10
    }.get(designation.lower(), 0)

    previous_engagement_score = 2.5 if previous_engagement else 0
    audience_score = {
        'local': 0,
        'national': 2.5,
        'international': 5
    }.get(audience.lower(), 0)

    demographics_score = 5 if demographics else 0
    honors_awards_score = 5 if honors_awards else 0
    publications_score = {
        0: 0,
        1: 5,
        2: 5,
        3: 10
    }.get(publications, 0)

    # Total score calculation
    total_score = (experience_score + education_score + serving_org_score + designation_score +
                   previous_engagement_score + audience_score + demographics_score +
                   honors_awards_score + publications_score)

    return total_score


def assign_badge(score):
    if score >= 85:
        return "Platinum"
    elif score >= 70:
        return "Gold"
    elif score >= 50:
        return "Silver"
    else:
        return "Bronze"


# Example input
experience_years = 6
education_degrees = 2

# serving_org_type = 'medium'
# File paths for the datasets
university_file = 'Badge_assignment\QSWUR2025.xlsx'
company_file = 'Badge_assignment\Top2000CompaniesGlobally.xlsx'
# Initialize the classifier object
classifier = OrganizationClassifier(university_file, company_file)
# Example usage
org_type_input = 'university'
organization_input = 'Harvard University'
result = classifier.classify_organization(org_type_input, organization_input)

serving_org_type = result['Classification']
# print(serving_org_type)


# designation = 'Mid-level'
# Initialize the classifier object
file_path = 'Badge_assignment\desig_rank.xlsx'
classifier = DesignationClassifier(file_path)
sector_input = 'Arts & Entertainment'
designation_input = 'Editor'
result = classifier.get_classification(sector_input, designation_input)

designation = result['Classification']
# print(designation)

previous_engagement = True
audience = 'national'
demographics = True
honors_awards = True
publications = 1

# Calculate score and assign badge
total_score = calculate_score(experience_years, education_degrees, serving_org_type, designation, 
                              previous_engagement, audience, demographics, honors_awards, publications)

badge = assign_badge(total_score)

print(f"Total Score: {total_score}")
print(f"Assigned Badge: {badge}")
