import sys
import pymysql
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class Db_GUI(QMainWindow):
   

    def __init__(self):
        super().__init__()
        uic.loadUi("myGUI.ui", self)
        #Defining global variables
        strError = 'Ocurrió un error'
        strOK = 'Todo marcha sobre ruedas'
        self.conection()        
        self.fn_comboBox_fill()
        self.tabs = self.tabWidget()
        self.tabs.currentChanged.connect(self.fn_comboBox_fill)

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

    def fn_tables(self):
        try: 
            cursor = db.cursor()
            consultAllTables = 'SHOW FULL TABLES FROM mundo_peludo;'
            cursor.execute(consultAllTables)
            result = cursor.fetchall()
            return result            
        except:
            self.status_label.setText(self.strError)
            return "Empty" 

    def fn_comboBox_fill(self):
        tables = self.fn_tables()
        if(tables != 'Empty'):
            #Imprimir bonito
            #El índice donde está el usuario en el TabWidget
            index = self.tabs.currentIndex()

            if(index == 0):
                comboBox = self.tables_cb()
            else:
                comboBox = self.tables_cb1()

            for row in tables:
                table = row[0]
                comboBox.addItem(table)                 



def main():    
    app = QApplication(sys.argv)
    GUI = Db_GUI()
    GUI.show()
    sys.exit(app.exec_())   

if __name__ == "__main__":
    main()