from flask import Flask, render_template, request, jsonify
import json

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

if __name__ == '__main__':
    app.run(debug=True)