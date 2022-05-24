from flask import Flask, request
import os
import pickle

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True

model = pickle.load(open('../data/finished_model.model','rb'))

@app.route('/', methods=['GET'])
def home():
    return "Modelo que Mide el Sentimiento de un Tweet"


@app.route('/api/v1/consulta', methods=['GET'])
def consulta():

    tweet = request.args.get('tweet', None)
    predictions = model.predict([tweet])[0]

    if predictions == 1:
        return  'Tweet de sentimiento negativo'
    elif predictions == 0:
        return 'Tweet de sentimiento positivo'
 

app.run()