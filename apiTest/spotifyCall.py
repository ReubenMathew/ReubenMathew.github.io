import easydbio
import flask
import simplejson
import pprint
import sys
import requests
import json

db = easydbio.DB({
  "database": "07380c98-9f91-4f29-8ed6-207c1771eb53",
  "token": "ec6e601c7c2c482abc666752fe744fa8"
})

def update():
	f = open('creds.csv', "r")
	creds = f.read().split("\n") # "\r\n" if needed
	creds = creds[0].split(',')

	CLIENT_ID = creds[0]
	CLIENT_SECRET = creds[1]

	grant_type = 'client_credentials'
	body_params = {'grant_type' : grant_type}

	url='https://accounts.spotify.com/api/token'
	response = requests.post(url, data=body_params, auth=(CLIENT_ID, CLIENT_SECRET)) 

	token_raw = simplejson.loads(response.text)
	token = token_raw["access_token"]
	headers = {"Authorization": "Bearer {}".format(token)}
	r = requests.get(url="https://api.spotify.com/v1/playlists/6o37RoezJdsZgk4Yi6OWrD/tracks", headers=headers)
	tracks = json.loads(r.text)
	peep = tracks['items'][-1]['track']

	trackName = peep['name']
	artist = peep['artists'][-1]['name']
	foo = db.Get('curr')
	db.Put('previous',foo)
	db.Put('curr',f'{trackName} by {artist}')
	print(trackName,'by',artist)
	print(db.List())