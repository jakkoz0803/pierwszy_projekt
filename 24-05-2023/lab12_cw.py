import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import PIL

ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()

df = pd.DataFrame(ts, columns=['wartosci'])
print(df)
df['Średnia krocząca'] = df.rolling(window=50).mean()
df.plot()
plt.legend()
plt.show()

x=np.random.randn(10000)
plt.hist(x,bins=50,facecolor='g',alpha=0.75,density=True )
plt.xlabel('Wartości')
plt.ylabel('Prawdopodobieśstwo')
plt.title('Histogram')
plt.grid()
plt.show()

df=pd.read_csv('dane.csv', header=0, sep=";", decimal=".")
print(df)
seria=df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
wedges,texts,autotext=plt.pie(x=seria,
                              labels=seria.index,
                              autopct=lambda pct:"{:.1f}%".format(pct),
                              textprops=dict(color='black'),
                              colors=['red','green'])
plt.title('Suma zamówień dla sprzedawców')
plt.legend(loc='lower right')
plt.ylabel('Procentowy wynik wartości zamówień')
plt.show()

sns.set(rc={'figure.figsize':(8,8)})
sns.lineplot(x=[1,2,3,4],y=[1,4,9,16],label='linia nr1',
             color='red',marker='o',linestyle=':')
sns.lineplot(x=[1,2,3,4],y=[2,5,10,17],label='linia nr2',
             color='green',marker='^',linestyle=':')
plt.xlabel('oś x')
plt.ylabel('oś y')
plt.title('Wykres liniowy')
plt.show()

s = pd.Series(np.random.randn(1000))
s = s.cumsum()
sns.set()
wykres  = sns.relplot(kind='line',data=s,label='linia')
wykres.fig.set_size_inches(8,6)
wykres.fig.suptitle('Wykres liniowy losowych danych')
wykres.set_xlabels('indeksy')
wykres.set_ylabels('wartości')
wykres.add_legend()
wykres.figure.subplots_adjust(left=0.1, right=0.9,bottom=0.1,top=0.9)
plt.show()

df=pd.read_csv('iris.data', header=0, sep=',', decimal='.')
print(df)
wykres = sns.lineplot(data=df, x=df.index, y='sepal length',
             hue='class')
wykres.set_xlabel('indeksy')
wykres.set_title('Wykres liniowy danych z Iris dataset')
wykres.legend(title='Rodzaj kwiatu')
plt.show()

data = {'a': np.arange(10),
      'c': np.random.randint(0,50,10),
      'd': np.random.randn(10)}
data['b'] = data['a'] + 10 * np.random.randn(10)
data['d'] = np.abs(data['d']) * 100
df = pd.DataFrame(data)
plot=sns.relplot(data=df, x='a', y='b', hue='c',
palette='bright', size='d',legend=True)
plot.set(xticks=data['a'])
plt.show()

data={'a': np.arange(50),
'c': np.random.randint(0,50,50),
'd': np.random.randn(50)}
data['b']= data['a'] +10 * np.random.randn(50)
data['d']=np.abs(data['d']) * 100
df=pd.DataFrame(data)
plot=sns.relplot(data=df, x='a', y='b', hue='c',
palette='bright', size='d',legend=True)
plot.set(xticks=data['a'])
plt.show()

data={'Kraj':['Belgia', 'Indie', 'Brazylia','Polska'],
'Stolica': ['Bruksela','New Delhi','Brasilla','Warszawa'],
'Kontynent':['Europa','Azja','Ameryka Południowa','Europa'],
'Populacja':[1231423,51235,12526,135312]}
df=pd.DataFrame(data)
plot=sns.barplot(data=df, x='Kontynent', y='Populacja',
hue='Kontynent', estimator=np.sum, errorbar=None,
dodge=False, palette=['red','green','blue'])
plot.legend(title='Populacja na kontynent')
plot.set(title='Wykres słupkowy')
plt.show()
