import sqlite3

db = sqlite3.connect('./database/bd_apicultor.db')
#cursor= db.cursor()

#insert
"""db.execute("INSERT INTO tb_apicultor (NDI, NOMBRES, APELLIDOS, PAIS, DEPARTAMENTO, CIUDAD O MUNICIPIO, NUMCOL, PRODUCCCION, TEMPERATURA, FECHATEMP) VALUES(1,"yil","zamb","colom","cundi","soacha",2,5,8,6)")
print("registro insertado exitosamente")"""
#update
#db.execute("UPDATE tb_apicultor SET APELLIDOS= 'MORA' WHERE NDI = 1") # ACTUALIZAR APELLIDO EN EL PRIMER REGISTRO
#delete
#db.execute("DELETE FROM tb_apicultor WHERE NDI = 1") # ELIMINAR PRIMER REGISTRO

#consultar

cursor = db.execute("SELECT * FROM tb_apicultor")
filas=cursor.fetchall()
for fila in filas:
    print(fila)


db.commit()
db.close()

"""def get_db():
    db = sqlite3.connect('./database/bd_apicultor.db')
    db.row_factory = sqlite3.Row
    return db

def init_db():
    db = get_db()
    with open('schema.sql', 'r') as f:
        db.executescript(f.read())
    db.close()"""
