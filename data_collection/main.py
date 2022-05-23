import twint
import nest_asyncio
import pandas as pd

nest_asyncio.apply()

# Configure
c = twint.Config()
c.Search = '@TheBridge_Tech'
# c.Store_json = True
# c.Output = '.data/raw_tweets.json'
c.Store_csv = True
c.Output = './data/raw_tweets.csv'
c.Since = '2022-01-01 00:00:00'
c.Hide_output = True
c.Debug = True

# Run
try:
    twint.run.Search(c)
except Exception as e:
    print(e)

data = pd.read_csv('../data/raw_tweets.csv')