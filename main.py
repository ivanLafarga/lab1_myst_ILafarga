
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import pandas as pd
import numpy as np
import data as dt
import functions as fn 
import visualizations as vis

datos = dt.primer_naftrac
precios = dt.prices

fechas = ['2020-01-31', '2020-02-28', '2020-03-31', '2020-04-30','2020-05-29','2020-06-30','2020-07-31',
'2020-08-31','2020-09-30','2020-10-30', '2020-11-30','2020-12-31','2021-01-29','2021-02-26','2021-03-31',
'2021-04-30','2021-05-31','2021-06-30','2021-07-30','2021-08-31','2021-09-30','2021-10-26','2021-11-30',
'2021-12-31','2022-01-26','2022-02-28','2022-03-31','2022-04-29','2022-05-31','2022-06-30','2022-07-29']

capital = 1000000

datos['Valor monetario'] = datos['Peso (%)']*capital 
datos['Comision'] = datos['Valor monetario']*0.00125

precios_cierre = precios.loc[fechas[0]]
lista_precios_cierre = []

for i in datos.index:
    lista_precios_cierre.append(precios_cierre[i])

datos['Precio cierre'] = lista_precios_cierre
datos['Títulos'] = np.floor(datos['Valor monetario']/datos['Precio cierre'])

inversion_pasiva = pd.DataFrame()

for i in fechas:
    inversion_pasiva[i] = precios.loc[i]*datos['Títulos']

df_final = pd.DataFrame()

df_final['Capital'] = inversion_pasiva.sum() + dt.cash_total*capital

df_final['Rendimiento'] = df_final['Capital'].pct_change()

df_final['Rendimiento acum'] = df_final['Rendimiento'].cumsum()

df_medidas = pd.DataFrame(index=['Rendimiento mensual acumulado', 'Rendimiento mensual promedio', 'Radio de sharpe'])


mensual_acumulado = df_final['Rendimiento acum'][-1]
mensual_promedio = df_final['Rendimiento'].mean()
radio_sharpe = (mensual_promedio - 0.0429)/df_final['Rendimiento'].std()

df_medidas['Inversion pasiva'] = [mensual_acumulado, mensual_promedio, radio_sharpe]