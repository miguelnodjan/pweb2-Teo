import sqlite3
def crear_baseDatos():
    conn = sqlite3.connect('imdb.db')
    c = conn.cursor()
    c.execute("CREATE TABLE bebidas (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) NOT NULL, marca VARCHAR(100) NOT NULL, añoExp INTEGER NOT NULL, contenidoML NOT NULL)")

    bebidas = [
        ('Coca-Cola', 'Coca-Cola', 2019, 1000),
        ('Fanta', 'Coca-Cola', 2019, 1000),
        ('Pepsi', 'Coca-Cola', 2019, 1000),
        ('Sprite', 'Coca-Cola', 2019, 1000),
        ('Coca-Cola Zero', 'Coca-Cola', 2019, 1000),
        ('Coca-Cola Light', 'Coca-Cola', 2019, 1000),
        ('Fanta Zero', 'Coca-Cola', 2019, 1000),
    ]
    c.executemany("INSERT INTO bebidas (nombre, marca, añoExp, contenidoML) VALUES (?, ?, ?, ?)", bebidas)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    crear_baseDatos()