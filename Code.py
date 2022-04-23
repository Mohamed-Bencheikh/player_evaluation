import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVR

class Code:
    def __init__(self) -> None:
        pass

    def preprocess():
        df = pd.read_csv("data.csv")
        df.dropna(axis=0,inplace=True)
        
        le = LabelEncoder()
        categorical_attributes = ['preferred_foot', 'attacking_work_rate', 'defensive_work_rate']
        for attr in categorical_attributes:
            df[attr] = le.fit_transform(df[attr])
        X = df.loc[:,"potential":"gk_reflexes"]
        Y = df["overall_rating"]
        return (X,Y)
        
    def prediction(lst = []):
        X,Y = Code.preprocess()

        model = SVR()
        model.fit(X,Y)            

        model.score(X,Y)
        vals = np.array(lst).reshape(1,-1)
        res = model.predict(vals)
        return res
    


