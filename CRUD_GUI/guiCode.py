import sys
import pymysql
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class Db_GUI(QMainWindow):
   

    def __init__(self):
        super().__init__()
        uic.loadUi("myGUI.ui", self)
        #Defining variables
        self.strError = 'Ocurrió un error'
        self.strOK = 'Todo marcha sobre ruedas'
                
        self.fn_comboBox_fill()        
        self.tabWidget.currentChanged.connect(self.fn_comboBox_fill)

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
            db = self.conection()
            cursor = db.cursor()
            consultAllTables = 'SHOW FULL TABLES FROM mundo_peludo;'
            cursor.execute(consultAllTables)
            result = cursor.fetchall()
            self.status_label.setText(self.strOK)
            return result            
        except:
            self.status_label.setText(self.strError)
            #bandera
            print('error')
            return "Empty"
        finally:
            db.close() 

    def fn_comboBox_fill(self):
        tables = self.fn_tables()
        if(tables != 'Empty'):
            #Imprimir bonito
            #El índice donde está el usuario en el TabWidget
            index = self.tabWidget.currentIndex()

            if(index == 0):
                #self.tables_cb() ComboBox 1
                for row in tables:
                    table = row[0]
                    self.tables_cb.addItem(table)                 

            else:
                #self.tables_cb1() ComboBox 2
                for row in tables:
                    table = row[0]
                    self.tables_cb1.addItem(table)                 


            


def main():    
    app = QApplication(sys.argv)
    GUI = Db_GUI()
    GUI.show()
    sys.exit(app.exec_())   

if __name__ == "__main__":
    main()