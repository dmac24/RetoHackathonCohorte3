from flask import Flask, request, redirect, url_for, render_template
import sqlite3

app = Flask(__name__)

# Conexión y creación de la base de datos
def init_sqlite_db():
    conn = sqlite3.connect('./database/bd_apicultor.db')
    cursor = conn.cursor()
    # Creación de la tabla si no existe (opcional)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tb_apicultor (
            NDI TEXT,
            NOMBRES TEXT,
            APELLIDOS TEXT,
            PAIS TEXT,
            DEPARTAMENTO TEXT,
            CIUDAD TEXT,
            NUMCOL TEXT,
            PRODUCCION TEXT,
            TEMPERATURA TEXT,
            FECHA TEXT,
            ESTACION TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_sqlite_db()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    ndi = request.form['NDI']
    nombre = request.form['inputName']
    apellido = request.form['inputLastName']
    pais = request.form['inputpais']
    departamento = request.form['inputdepartamento']
    ciudad = request.form['inputciudad']
    numerodecol = request.form['inputnumcol']
    produccion = request.form['inputproduccion']
    temperatura = request.form['inputtemperatura']
    fecha = request.form['inputfecha']
    estacion = request.form['inputState']

    # Guardar los datos en la base de datos correcta
    conn = sqlite3.connect('./database/bd_apicultor.db')
    cursor = conn.cursor()

    # Valores
    cursor.execute("INSERT INTO tb_apicultor (NDI, NOMBRES, APELLIDOS, PAIS, DEPARTAMENTO, CIUDAD, NUMCOL, PRODUCCION, TEMPERATURA, FECHA, ESTACION) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                   (ndi, nombre, apellido, pais, departamento, ciudad, numerodecol, produccion, temperatura, fecha, estacion))

    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
