import pickle 
from functions import read_data, top_tweets

model = pickle.load(open('./model/finished_model.model', 'rb'))
df = read_data('./data/clean_tweets.csv')
x_test = top_tweets(df,3) 

pred = model.predict(x_test)

