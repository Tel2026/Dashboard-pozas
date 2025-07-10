from flask import Flask, render_template, request, jsonify
import json
import os
app = Flask(__name__)

@app.route('/')
def index():
    with open('data.json') as f:
        data = json.load(f)
    pozas = list(data.keys())
    return render_template('index.html', pozas=pozas)

@app.route('/poza/<nombre>')
def get_poza(nombre):
    with open('data.json') as f:
        data = json.load(f)
    bombas = data.get(nombre, [])
    return jsonify(bombas)
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port, debug=True)
