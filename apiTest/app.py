from flask import Flask, request
from spotifyCall import update
import time
import easydbio

app = Flask(__name__)


@app.route('/update')
def update_task():
	update()
	return "DB updated!"

@app.route('/view')
def view_task():
	return db.Get('curr')