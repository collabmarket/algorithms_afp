import pandas_datareader.data as web
import Quandl
from datetime import datetime

print "[INFO]--" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "--" + "get_quandl" + "--" + "INIT"

with open('token.txt', 'rU') as f:
    token = f.readline().rstrip('\n')

# Indicadores de Riesgo sistemico
dow = Quandl.get('BCB/UDJIAD1', authtoken=token)
wti = Quandl.get('EIA/PET_RWTC_D', authtoken=token)
fedrate = web.DataReader("FEDFUNDS", 'fred', start=datetime(1955,1,1))
money = web.DataReader("BOGMBASEW", 'fred', start=datetime(1976,1,1))
debt = web.DataReader("GFDEGDQ188S", 'fred', start=datetime(1966,1,1))
# Riesgo de tipo de cambio (solo para mostrar el pobre uso de derivados en 2009)
usdclp = Quandl.get("CURRFX/USDCLP", authtoken=token)

# Guarda datos
outdir = 'data_quandl/'
# Opciones escrituda de archivos csv
karg_csv = dict(sep=';', decimal=',')
dow.to_csv(outdir + 'dow.csv', **karg_csv)
wti.to_csv(outdir + 'wti.csv', **karg_csv)
fedrate.to_csv(outdir + 'fedrate.csv', **karg_csv)
usdclp.to_csv(outdir + 'usdclp.csv', **karg_csv)
money.to_csv(outdir + 'money.csv', **karg_csv)
debt.to_csv(outdir + 'debt.csv', **karg_csv)

print "[INFO]--" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "--" + "get_quandl" + "--" + "DONE"
