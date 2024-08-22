"""import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

def generate_dashboard():
    df = pd.read_csv('data/pollen_availability.csv')

    plt.figure(figsize=(12, 6))
    plt.plot(df['month'], df['availability'])
    plt.title('Disponibilidad de Polen a lo largo del año')
    plt.xlabel('Mes')
    plt.ylabel('Disponibilidad')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    return {'dashboard_image': base64.b64encode(img.getvalue()).decode()}"""