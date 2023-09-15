#--Carga los datos usando tu lector de csv o con pandas. Es recomendable hacerlo con pandas.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('COVID19MEXICO_Tarea2.csv')

#--Verifica la cantidad de datos que tienes, las variables que contiene cada vector de datos e identifica el tipo de variables.

filtro_60 = df[(df['EDAD'] > 60) & (df['EDAD'] )]
#//Se aplica un filtro para obtener los datos de las personas mayores a 60 años

filtro_60['FECHA_INGRESO'] = pd.to_datetime(filtro_60['FECHA_INGRESO'])
filtro_60 = filtro_60.sort_values(by='FECHA_INGRESO')
filtro_60.to_csv('archivo_ordenado.csv', index=False)
df2 = pd.read_csv('archivo_ordenado.csv')
print(df2['FECHA_INGRESO'])

#--Analiza las variables para saber que representa cada una y en que rangos se encuentran.
#--Si la descripción del problema no te lo indica, utiliza el máximo y el mínimo para encontrarlo.
sns.countplot(data=df2, x ='FECHA_INGRESO')

plt.ylabel('Adultos mayores a 60 años')
plt.xlabel('Fecha de ingreso del Paciente')
plt.title('Cantidad de pacientes mayores a 60 años ingresados por fecha')

plt.show()

#Basándose en la media, mediana y desviación estándar de cada variable, que conclusiones puedes entregar de los datos.
print('\n')
mediana_ = filtro_60['EDAD'].median()
media_ = filtro_60['EDAD'].mean()
desviacion_ = filtro_60['EDAD'].std()
print('La mediana de edades es: ', mediana_)
print('La media de edades es : ', media_)
print('La desviación estándar de edades es: ', desviacion_)
