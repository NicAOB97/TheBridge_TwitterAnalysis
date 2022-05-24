# Función read_data
import pandas as pd
from nltk.corpus import stopwords

def read_data(url):
    '''Lee los datos de la dirección proporcionada y devuelve un data frame'''
    df = pd.read_csv(url)
    return df

def top_tweets(df, number=3):
    '''ordena los tweets segun su impacto y devuelve el numero especificado del tweets del ranking'''
    df['total_effect'] = df['retweets_count']+df['replies_count']+df['likes_count']
    top_tweets = df.sort_values('total_effect', ascending = False)
    top = top_tweets.iloc[0:number]
    tweets = top['tweet']
    return tweets

def remove_stopwords(text):
    '''Elimina las palabras como que no aportan valor al contenido de la frase como puede ser "la" '''
    spanish_stopwords = stopwords.words('spanish')
    return " ".join([word for word in text.split() if word not in spanish_stopwords])
