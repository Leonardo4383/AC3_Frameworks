import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/api/upper', methods=['POST'])
def upper():
    json = request.get_json()
    primeiro_nome = json['first'].upper()
    ultimo_nome = json['last'].upper()
    valor = json['combo'].upper()
    return jsonify(primeiro_nome=primeiro_nome,ultimo_nome=ultimo_nome,valor=valor)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)