import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/Honey 2013-2021.csv')
print(df.info())
print(df.head())
print(df.describe())


"""import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def suggest_reactivation(data):
    # Cargar y procesar datos históricos
    df = pd.read_csv('/content/Honey 2013-2021.csv')

    # Preparar características y objetivo
    X = df[['month', 'temperature', 'rainfall']]
    y = df['production']

    # Entrenar modelo
    model = RandomForestRegressor()
    model.fit(X, y)

    # Predecir mejor momento para reactivar
    predictions = model.predict(data)
    best_time = predictions.argmax()

    return {'best_reactivation_time': best_time}"""