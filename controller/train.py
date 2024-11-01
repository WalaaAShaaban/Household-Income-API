import sys
sys.path.append('../Household-Income-API')
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib


def train(dataset):
    # Read the data
    df = pd.read_csv(dataset)
    X = df.drop('Income', axis=1)
    y = df['Income']

    # Encode the categorical variables
    cat_cols = df.select_dtypes("object").columns
    le = LabelEncoder()
    for col in cat_cols:
        X[col] = le.fit_transform(X[col])
    print(X.iloc[10])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Create a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)


    # Save the model
    joblib.dump(model, 'model/model.pkl')
    


