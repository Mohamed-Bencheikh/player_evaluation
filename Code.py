# importation des libraries:
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVR
import pickle as pk
# la classe Code
class Code:
    def __init__(self) -> None:
        pass
# le pre-traitement des données:
    def preprocess():
        # charger les données depuis un fichier CSV dans un dataframe df:
        df = pd.read_csv("data.csv")
        # effacer les lignes ayant des attributs manquants:
        df.dropna(axis=0,inplace=True)
        # convertir les attributs catégoriques en valeurs numériques
        le = LabelEncoder()
        categorical_attributes = ['preferred_foot', 'attacking_work_rate', 'defensive_work_rate']
        for attr in categorical_attributes:
            df[attr] = le.fit_transform(df[attr])
        X = df.loc[:,"potential":"gk_positioning"]
        Y = df["overall_rating"]
        return (X,Y)
# la fonction de prediction: 
    def prediction(lst = []):
        X,Y = Code.preprocess()

        model = pk.load(open('model.pkl','rb'))
        model.fit(X,Y)            
        vals = np.array(lst).reshape(1,-1)
        res = model.predict(vals)
        return res
    


