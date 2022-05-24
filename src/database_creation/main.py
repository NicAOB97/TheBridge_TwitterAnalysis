import sqlite3
import pandas as pd

df = pd.read_csv('../data/clean_tweets.csv')

connt = sqlite3.connect('../data/tweets.db')
connu = sqlite3.connect('../data/users.db')

ct = connt.cursor()
cu = connu.cursor()

ct.execute(
    """CREATE TABLE IF NOT EXISTS tweets(
        id VARCHAR(255) PRIMARY KEY,
        tweet TEXT NOT NULL,
        created_at DATE, 
        user_id VARCHAR(255),
        retweets_count INTEGER,
        replies_count INTEGER,
        likes_count INTEGER,
        quote_url VARCHAR(255)
        )"""
    )

cu.execute(
    """CREATE TABLE IF NOT EXISTS users(
    user_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    username VARCHAR(255),
    )"""
    )

sql = '''SELECT * FROM tweets'''
ct.execute(sql)