import pandas as pd
import matplotlib.pyplot as plt

csv= pd.read_csv('data\Honey 2013-2021.csv', sep=",")
dataframe=pd.DataFrame(csv[list(set(["stateidnum","state","numcol","yieldpercol","totalprod","stocks","priceperlb","prodvalue","year"]))])
#dataframe=pd.DataFrame(csv[list(set(csv.columns)- set(["numcol","yieldpercol"]))])
#print(dataframe)
rendimiento=dataframe["yieldpercol"].value_counts()
numerocolmenas=dataframe["numcol"].value_counts().head()
print(numerocolmenas)


#GRAFICA 1
plt.subplot(1,2,1) # una fila dos columnas posicion 1
numerocolmenas.plot(kind="pie",autopct='%1.01f%%') 
plt.title("numcol")

#GRAFICA 2
plt.subplot(1,2,2) # una fila dos columnas posicion 2
rendimiento.plot(kind="bar") 
plt.title("yieldpercol")


plt.suptitle("grafica numero de colmenas y su rendimiento")
plt.show()