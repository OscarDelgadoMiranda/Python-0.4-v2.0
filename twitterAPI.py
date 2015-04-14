#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Oscar Delgado Miranda y Miguel Angel Perez Garcia'
import twitter
import io
import json

#Funcion para la conexion
def oauth_login():
    CONSUMER_KEY = '2TgBivZJndnZlQeuTgpm3m7oi'
    CONSUMER_SECRET = 'ta009qc3iUkH1fgZ0kwuGctqY4Ev3sQaVQc4bJ1swvA3wc18AV'
    OAUTH_TOKEN = '3159942879-LUIIk5ce2g9C4NbjJa8M9ZjV23hx9RUB6KJ6AHc'
    OAUTH_TOKEN_SECRET = '68PuK047NH2dM5FjFMqpeN8RUDVfkI6NfYTX8TapTjz8V'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

#Funcion para grabar la informacion en formato JSON
def save_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

#Funcion para leer el fichero JSON
def load_json(filename):
    with io.open('{0}.json'.format(filename),encoding='utf-8') as f:
        return f.read()

def getTweetsSearch(busqueda):
	twitter_api =  oauth_login()
	#Limitamos la busqueda a Espana

	tweets = twitter_api.search.tweets(q=busqueda, count=1000, geocode='36.516380894202264,-6.282446299999947,500km')

	aux = json.dumps(tweets, indent = 1)
	it = json.loads(aux)

	resultado = []
	for i in it['statuses']:
		if i['coordinates'] is not None:
			resultado.append(i['coordinates']['coordinates'][1])
			resultado.append(i['coordinates']['coordinates'][0])

	resultado = zip(resultado[0::1], resultado[1::2])
	return resultado
