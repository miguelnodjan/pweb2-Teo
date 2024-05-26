from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def query_db(query, args=(), one=False):
    conn = sqlite3.connect('imdb.db')
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/bebidas', methods=['GET'])
def get_bebidas():
    bebidas = query_db('SELECT * FROM bebidas')
    return jsonify(bebidas)

@app.route('/bebida/<int:bebida_id>', methods=['GET'])
def get_bebida(bebida_id):
    bebida = query_db('SELECT * FROM bebidas WHERE id = ?', [bebida_id], one=True)
    return jsonify(bebida)

@app.route('/bebida', methods=['POST'])
def add_bebida():
    new_bebida = request.json
    conn = sqlite3.connect('imdb.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO bebidas (nombre, marca, añoExp, contenidoML) VALUES (?, ?, ?, ?)', 
                (new_bebida['nombre'], new_bebida['marca'], new_bebida['añoExp'], new_bebida['contenidoML']))
    conn.commit()
    conn.close()
    return jsonify(new_bebida), 201

if __name__ == '__main__':
    app.run(debug=True)
