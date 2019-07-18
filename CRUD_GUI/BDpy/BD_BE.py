import sys
import pymysql
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class BD_GUI (QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("BD_GUI.ui", self)
        self.btn_create.clicked.connect(self.fn_create)
        self.btn_read.clicked.connect(self.fn_read)
        self.btn_update.clicked.connect(self.fn_update)
        self.btn_delete.clicked.connect(self.fn_delete)
        
    def db_init(self):
        try:
            db = pymysql.connect("localhost","root","","automatasii")
            self.fn_imprimir("Conexión establecida...")
            return db
        except:
            self.fn_imprimir("Error, no se estableció la conexión...")

    def fn_imprimir(self, mensaje):
        self.lbl_message.setText(mensaje)

    def fn_create(self):
        db = self.db_init()
        if (self.lbl_message.text() == "Conexion establecida..."):  
            try:
                cursor = db.cursor()
                clave = self.txt_clave.text()
                nombre = self.txt_nombre.text()
                sqlinsertar = "insert into keyword values({0}, {1});".format(clave, nombre)
                cursor.execute(sqlinsertar)
                db.commit()
                cursor.close()
                db.close()
                self.fn_imprimir("Datos Guardados con exito")
            except:
                self.fn_imprimir("Error al guardar")
    
    def fn_read(self):
        db = self.db_init()
        if (self.lbl_message.text() == "Conexion establecida..."):  
            try:
                cursor = db.cursor()
                sqlbuscar = "select * from keyword;"
                cursor.execute(sqlbuscar)
                resultado = cursor.fetchall()
                self.tbl_datos.setRowCount(0)
                for fila_num, fila_dato in enumerate(resultado):
                    self.tbl_datos.insertRow(fila_num)
                    for col_num, dato in enumerate(fila_dato):
                        self.tbl_datos.setItem(fila_num, col_num, QtWidgets.QtableWidgetItem(str(dato)))
                cursor.close()
                db.close()
                self.fn_imprimir("Datos leidos con exito")
            except:
                self.fn_imprimir("Error al leer")
    
    def fn_update(self):
        db = self.db_init()
        if (self.lbl_message.text() == "Conexion establecida..."):  
            try:
                cursor = db.cursor()
                clave = self.txt_clave.text()
                nombre = self.txt_nombre.text()
                sqlmodificar = "update keyword set nombre = {1} where clave = {0};".format(clave, nombre)
                cursor.execute(sqlmodificar)
                db.commit()
                cursor.close()
                db.close()
                self.fn_imprimir("Datos Guardados con exito")
            except:
                self.fn_imprimir("Error al guardar")

    def fn_delete(self):
        db = self.db_init()
        if (self.lbl_message.text() == "Conexion establecida..."):  
            try:
                cursor = db.cursor()
                clave = self.txt_clave.text()
                sqlborrar = "delete from keyword where clave = {0};".format(clave)
                cursor.execute(sqlborrar)
                db.commit()
                cursor.close()
                db.close()
                self.fn_imprimir("Datos Guardados con exito")
            except:
                self.fn_imprimir("Error al guardar")


def main ():
    app = QApplication(sys.argv)
    GUI = BD_GUI()
    GUI.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
