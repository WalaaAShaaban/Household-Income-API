from pydantic import BaseModel


class RequestIncome(BaseModel):
    Age : int
    Education_Level : str
    Occupation : str
    Number_of_Dependents : int
    Location : str
    Work_Experience : int
    Marital_Status : str
    Employment_Status : str
    Household_Size : int
    Homeownership_Status : str
    Type_of_Housing : str
    Gender : str
    Primary_Mode_of_Transportation : str
    
