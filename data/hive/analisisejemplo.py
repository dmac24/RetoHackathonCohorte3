import pandas as pd
import matplotlib.pyplot as plt

csv= pd.read_csv('data\Honey 2013-2021.csv', sep=",")
dataframe=pd.DataFrame(csv[list(set(["stateidnum","state","numcol","yieldpercol","totalprod","stocks","priceperlb","prodvalue","year"]))])
#dataframe=pd.DataFrame(csv[list(set(csv.columns)- set(["numcol","yieldpercol"]))])
#print(dataframe)
produccion=dataframe["totalprod"].value_counts()
years=dataframe["year"].value_counts().head()
print(produccion)


#GRAFICA 1
plt.subplot(1,2,1) # una fila dos columnas posicion 1
produccion.plot(kind="pie",autopct='%1.01f%%') 
plt.title("totalprod")

#GRAFICA 2
plt.subplot(1,2,2) # una fila dos columnas posicion 2
years.plot(kind="bar") 
plt.title("year")


plt.suptitle("grafica años y su total de producción")
plt.show()