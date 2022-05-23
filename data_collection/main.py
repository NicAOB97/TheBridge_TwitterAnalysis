import twint
import nest_asyncio
import pandas as pd

# utiliza la libreria de TWINT para escrappear twitter y obtener la informacion deseada

nest_asyncio.apply()
# Configuracion
c = twint.Config()
c.Search = '@TheBridge_Tech'
# Guardar en CSV
c.Store_csv = True
c.Output = '../data/raw_tweets.csv'
# especificar fecha
c.Since = '2022-01-01 00:00:00'
c.Hide_output = True
c.Debug = True

# Run
try:
    twint.run.Search(c)
except Exception as e:
    print(e)
