from twitterAPI import *

def getTweetsSearch(busqueda):
	twitter_api =  oauth_login()

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
