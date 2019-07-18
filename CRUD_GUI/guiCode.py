import sys
import pymysql
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class Db_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("myGUI.ui", self)
        self.conection()

    #Conexión
    def conection(self):
        try:
            #Cadena de conexión
            db = pymysql.connect("localhost","root","","mundo_peludo")
            message = 'Conexión a la base de datos exitosa!'
            return db
        except:
            message = 'La conexión falló!'            
            self.tabWidget.setEnabled(False)
        finally:
            self.status_label.setText(message)

    def fn_create(self):



def main():    
    app = QApplication(sys.argv)
    GUI = Db_GUI()
    GUI.show()
    sys.exit(app.exec_())   

if __name__ == "__main__":
    main()