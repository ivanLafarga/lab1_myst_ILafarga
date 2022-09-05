
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: data.py : python script for data collection                                                 -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
import pandas as pd
import yfinance as yf
dict_test = {'key_a': 'a', 'key_b': 'b'}

# Leer primer archivo, hacer tercera fila los nombres de las columnas, solo usar primera y cuarta columna
primer_naftrac = pd.read_csv(r'files/NAFTRAC_2020_2022/NAFTRAC_20200131.csv', header=2, usecols=[0,3])
primer_naftrac['Peso (%)'] = primer_naftrac['Peso (%)']/100
# tickers a borrar
borrar = ["KOFUBL", "BSMXB","IENOVA*"]

# Obtener el indice de los tickers que voy a borrar
indices_borrar = primer_naftrac[primer_naftrac['Ticker'].isin(borrar)].index
pesos_cash = primer_naftrac[primer_naftrac['Ticker'].isin(borrar)]['Peso (%)'].sum()

# Suma cash
cash_total = (primer_naftrac[primer_naftrac['Ticker'] == 'MXN']['Peso (%)'] + pesos_cash).values

# Eliminar indices del dataframe 
primer_naftrac.drop(indices_borrar, axis=0, inplace=True)
primer_naftrac.drop(36, inplace=True)
primer_naftrac.drop(34, inplace=True)

tickers = ['AMXL.MX','FEMSAUBD.MX','GFNORTEO.MX','WALMEX.MX','GMEXICOB.MX','CEMEXCPO.MX','TLEVISACPO.MX','GAPB.MX','ELEKTRA.MX', 'KIMBERA.MX',
'ASURB.MX','BIMBOA.MX','OMAB','AC','GFINBURO.MX','PINFRA.MX','GRUMAB.MX','ORBIA.MX','ALFAA.MX','GCARSOA1.MX',
'PE&OLES.MX','ALSEA.MX','BBAJIOO.MX','GENTERA.MX','MEGACPO.MX','LIVEPOLC-1.MX','BOLSAA.MX','CUERVO.MX','LABB.MX','GCC',
'RA','ALPEKA.MX' ]


prices = pd.DataFrame()

for ticker in tickers:
    data = yf.download(ticker, start='2020-01-01', end='2022-08-01')['Close']
    prices[ticker] = data

diccionario_remplazar = {'AMXL': 'AMXL.MX','FEMSAUBD':'FEMSAUBD.MX','GFNORTEO':'GFNORTEO.MX','WALMEX*':'WALMEX.MX','GMEXICOB':'GMEXICOB.MX','CEMEXCPO':'CEMEXCPO.MX',
'TLEVISACPO':'TLEVISACPO.MX','GAPB':'GAPB.MX','ELEKTRA*':'ELEKTRA.MX','KIMBERA':'KIMBERA.MX','ASURB':'ASURB.MX','BIMBOA':'BIMBOA.MX','OMAB':'OMAB','AC*':'AC',
'GFINBURO':'GFINBURO.MX','PINFRA*':'PINFRA.MX','GRUMAB':'GRUMAB.MX','ORBIA*':'ORBIA.MX','ALFAA':'ALFAA.MX','GCARSOA1':'GCARSOA1.MX','PE&OLES*':'PE&OLES.MX',
'ALSEA*':'ALSEA.MX','BBAJIOO':'BBAJIOO.MX','GENTERA*':'GENTERA.MX','MEGACPO':'MEGACPO.MX','LIVEPOLC.1':'LIVEPOLC-1.MX','BOLSAA':'BOLSAA.MX','CUERVO*':'CUERVO.MX',
'LABB':'LABB.MX','GCC*':'GCC','RA':'RA',"ALPEKA":'ALPEKA.MX'}

primer_naftrac.replace(diccionario_remplazar, inplace=True)
primer_naftrac.index = primer_naftrac['Ticker']