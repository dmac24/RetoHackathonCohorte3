from flask import Flask, request, redirect, url_for, send_from_directory, render_template
import sqlite3

app = Flask(__name__)

# Configuración de la base de datos
def init_sqlite_db():
    conn = sqlite3.connect('./database/bd_apicultor.db')
    cursor = conn.cursor()
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
    # Redirigir al inicio de sesión o a la página principal
    return render_template('index.html')

@app.route('/home')
def home():
    # Renderiza la página de registro
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

    conn = sqlite3.connect('./database/bd_apicultor.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tb_apicultor (NDI, NOMBRES, APELLIDOS, PAIS, DEPARTAMENTO, CIUDAD, NUMCOL, PRODUCCION, TEMPERATURA, FECHA, ESTACION) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                   (ndi, nombre, apellido, pais, departamento, ciudad, numerodecol, produccion, temperatura, fecha, estacion))

    conn.commit()
    conn.close()

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
