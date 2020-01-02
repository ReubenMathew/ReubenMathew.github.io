from flask import Flask, render_template, jsonify
import easydbio

app = Flask(__name__,
			static_folder = './dist/static',
			template_folder = './dist')
app.config.from_object('config')

db = easydbio.DB({
  "database": app.config['DATABASE'],
  "token": app.config['TOKEN']
})

@app.route('/api/spotify')
def db_call():
	return jsonify(db.List())

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")