import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/Honey 2013-2021.csv')


#datos descriptivos
print(df.info())
print(df.head(10))
print(df.describe())

# grafica histograma 
df.hist()
plt.title('Histograma del total de la produccíon')
plt.xlabel('totalprod')
plt.show()


#csv= pd.read_csv('data\Honey 2013-2021.csv', sep=",")
"""dataframe=pd.DataFrame(csv[list(set(["stateidnum","state","numcol","yieldpercol","totalprod","stocks","priceperlb","prodvalue","year"]))])

dataframe.hist("totalprod", bins=6)"""

