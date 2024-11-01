import sys
sys.path.append('../Household-Income-API')
import pandas as pd

df = pd.read_csv('model/income.csv')
print(df['Primary_Mode_of_Transportation'].unique())
'''

df['Education_Level'] = ["Master's" 'High School' "Bachelor's" 'Doctorate']
df['Occupation'] = ['Technology' 'Finance' 'Others' 'Education' 'Healthcare']
df['Location'] = ['Urban' 'Rural' 'Suburban']
df['Marital_Status']  = ['Married' 'Single' 'Divorced']
df['Employment_Status'] = df['Employment_Status']
df['Homeownership_Status'] = ['Own' 'Rent']
df['Type_of_Housing']= ['Apartment' 'Single-family home' 'Townhouse']
df['Gender'] = ['Male' 'Female']
df['Primary_Mode_of_Transportation'] = ['Public transit' 'Biking' 'Car' 'Walking']
'''

'''
mappings = {
    'Education_Level': {"High School": 0, "Bachelor's": 1, "Master's": 2, 'Doctorate': 3},
    'Occupation': {'Technology': 0, 'Finance': 1, 'Others': 2, 'Education': 3, 'Healthcare': 4},
    'Location': {'Urban': 0, 'Rural': 1, 'Suburban': 2},
    'Marital_Status': {'Married': 0, 'Single': 1, 'Divorced': 2},
    'Employment_Status': {'Employed': 0, 'Unemployed': 1, 'Student': 2, 'Retired': 3},
    'Homeownership_Status': {'Own': 0, 'Rent': 1},
    'Type_of_Housing': {'Apartment': 0, 'Single-family home': 1, 'Townhouse': 2},
    'Gender': {'Male': 0, 'Female': 1},
    'Primary_Mode_of_Transportation': {'Public transit': 0, 'Biking': 1, 'Car': 2, 'Walking': 3}
}

# Apply the mappings to each column
for col, mapping in mappings.items():
    df[col] = df[col].map(mapping)
    '''