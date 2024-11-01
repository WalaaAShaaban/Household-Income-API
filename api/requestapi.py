import sys
sys.path.append('../Household-Income-API')
import fastapi
import joblib
from model.RequestIncome import RequestIncome
import controller.train as train




router = fastapi.APIRouter()
train.train('model/income.csv')

model = joblib.load('model/model.pkl')

@router.get("/")
def welcome():
    return {'message' : 'Welcome Income API'}


@router.post("/predict")
def predict_income(request : RequestIncome):
    
    mappings = {
    'Education_Level': {"High School": 0, "Bachelor's": 1, "Master's": 2, 'Doctorate': 3},
    'Occupation': {'Technology': 0, 'Finance': 1, 'Others': 2, 'Education': 3, 'Healthcare': 4},
    'Location': {'Urban': 0, 'Rural': 1, 'Suburban': 2},
    'Marital_Status': {'Married': 0, 'Single': 1, 'Divorced': 2},
    'Employment_Status': {'Full-time':0 ,'Self-employed':1, 'Part-time':2},
    'Homeownership_Status': {'Own': 0, 'Rent': 1},
    'Type_of_Housing': {'Apartment': 0, 'Single-family home': 1, 'Townhouse': 2},
    'Gender': {'Male': 0, 'Female': 1},
    'Primary_Mode_of_Transportation': {'Public transit': 0, 'Biking': 1, 'Car': 2, 'Walking': 3}
}
    # reverse_mappings = {key: {v: k for k, v in value.items()} for key, value in mappings.items()}
   
    prediction = model.predict([[
            request.Age,
            mappings['Education_Level'][request.Education_Level],
            mappings['Occupation'][request.Occupation],
            request.Number_of_Dependents,
            mappings['Location'][request.Location],
            request.Work_Experience,
            mappings['Marital_Status'][request.Marital_Status],
            mappings['Employment_Status'][request.Employment_Status],
            request.Household_Size,
            mappings['Homeownership_Status'][request.Homeownership_Status],
            mappings['Type_of_Housing'][request.Type_of_Housing],
            mappings['Gender'][request.Gender],
            mappings['Primary_Mode_of_Transportation'][request.Primary_Mode_of_Transportation]
            ]])
    
    return {'prediction' : prediction[0]}