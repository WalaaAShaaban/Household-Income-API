import sys
sys.path.append('../Household-Income-API')
import joblib
from api.requestapi import router
from fastapi import FastAPI

# read the model
model = joblib.load('model/model.pkl')

app = FastAPI()
app.include_router(router)


