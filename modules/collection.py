"""import pandas as pd
import numpy as np

def optimal_collection_times(data):
    df = pd.DataFrame(data)

    # Calcular la media móvil de producción
    df['rolling_mean'] = df['production'].rolling(window=7).mean()

    # Identificar picos de producción
    peaks = df[df['rolling_mean'] > df['rolling_mean'].quantile(0.75)]

    return {'optimal_collection_days': peaks['date'].tolist()}"""