##ejrcicio 9
import matplotlib.pyplot as plt 
import pandas as pd 
from statistics import mean

df0 = pd.read_csv('Datos.txt', header=0, delim_whitespace=True)

pd.set_option('display.max_rows', df0.shape[0]+1)

df0['Tiempo1'] = df0['Tiempo1'].replace('NaN','0.00')

print(mean(df0['Tiempo1']))
