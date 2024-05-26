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

@app.route('/bebidas',  methods=['GET'])
def get_bebidas():
    bebidas = query_db('select * from bebidas')
    return jsonify(bebidas)

@app.route('/bebidas/<int:bebida_id>',  methods=['GET'])
def get_bebida(bebida_id):
    movie = query_db('select * from bebidas where id = ?', [bebida_id], one= True)
    return jsonify(movie)
def addbebida():
    bebidaNew = request.json
    conn = sqlite3.connect('imd.db')
    cur = conn.cursor()
    cur.execute('insert into bebidas (nombre, marca, añoExp, contenidoML) Values(?, ?, ?, ?)', (bebidaNew['nombre'], bebidaNew['marca'], bebidaNew['añoExp'], bebidaNew['contenidMl']))
    conn.commit()
    conn.close()
    return jsonify(bebidaNew)
if __name__ == '__main__':
    app.run(debug=True)
