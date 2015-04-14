#!/usr/bin/python
# -*- coding: utf-8 -*-

#Grupo 13:
#Oscar Delgado Miranda
#Miguel Angel Perez Garcia

from flask import Flask, render_template
from flask import request
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map
from informacion import *

app = Flask(__name__)
GoogleMaps(app)

#Creacion del mapa
@app.route("/buscar", methods=['POST'])
def buscar():
	termino = request.form['text'] 
	coordenadas = getTweetsSearch(termino)
	
	mymap = Map(
		identifier="view-side",
		lat=36.516380894202264,
		lng=-6.282446299999947,
		markers=coordenadas,
		style="height:800px;width:800px;margin:0;"
	) 
	return render_template('mapa.html', mymap=mymap)

@app.route("/")
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)
