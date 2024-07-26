#%%
#Importamos las librerias
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from typing import List, Union
from sklearn.preprocessing import StandardScaler
#%%
#Cargamos el modelo
model_class = joblib.load('model_class.pkl')
#Cargamos el LabelEncoder
LabelEncoder = joblib.load('LabelEncoder.pkl')
#%%
# Inicializar la aplicación FastAPI
app = FastAPI()

#Definimos las variables de entrada al modelo
class PredictionInput(BaseModel):
    SeniorCity: Union[int, float]
    Partner: Union[int, float]
    Dependents: Union[int, float]
    Service1: Union[int, float]
    Service2: Union[int, float]
    Security: Union[int, float]
    OnlineBackup: Union[int, float]
    DeviceProtection: Union[int, float]
    TechSupport: Union[int, float]
    Contract: Union[int, float]
    PaperlessBilling: Union[int, float]
    PaymentMethod: Union[int, float]
    Charges: Union[int, float]
    Demand: Union[int, float]

#Salida
class PredictionOutput(BaseModel):
    class_prediction: str

#Diccionario para convertir predicciones numéricas a etiquetas
class_labels = {0: "Alpha", 1: "Betha"}

#Ruta
@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    # Convertir el JSON en un array de numpy
    features_array = np.array([[
        input_data.SeniorCity,
        input_data.Partner,
        input_data.Dependents,
        input_data.Service1,
        input_data.Service2,
        input_data.Security,
        input_data.OnlineBackup,
        input_data.DeviceProtection,
        input_data.TechSupport,
        input_data.Contract,
        input_data.PaperlessBilling,
        input_data.PaymentMethod,
        input_data.Charges,
        input_data.Demand
    ]])

    #Procesamos las variables
    df_features = pd.DataFrame(features_array,columns=list(LabelEncoder.keys()))

    df_features_new = df_features.copy()
    df_features_new.drop(['autoID','Demand','Charges','Class'], axis = 1, inplace=True)
    #Convertimos categorias a valores
    for column in df_features_new.columns:
        le = LabelEncoder[column]
        df_features_new[column] = le.transform(df_features_new[column])
    #Agregamos a "to_predict" el Demand pronosticado
    df_features_new['Demand'] = df_features['Demand']
    df_features_new['Charges'] = df_features['Charges']
    scaler = StandardScaler()
    Var_scaled_pred = scaler.fit_transform(df_features_new[['Charges','Demand']])
    #Agregamos los valores escalados al dataframe
    df_features_new['Charges'] = Var_scaled_pred[:,0]
    df_features_new['Demand'] = Var_scaled_pred[:,1]

    #Predecimos
    class_pred_num = model_class.predict(df_features_new.values)[0]

    #Devolvemos a los datos originales 
    class_pred_label = class_labels[class_pred_num]

    return PredictionOutput(class_prediction=class_pred_label)