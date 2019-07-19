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
        #Filling comboBox        
        self.fn_comboBox_fill()        
        self.tabWidget.currentChanged.connect(self.fn_comboBox_fill)
        #Buttons clicked
        self.show_button.clicked.connect(self.fn_show)
        #self.insert_button.clicked.connect(self.fn_insert)

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
            return "Empty"
        finally:
            db.close() 

    def fn_comboBox_fill(self):
        tables = self.fn_tables()
        if(tables != 'Empty'):           
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

    def fn_show(self):
        try:
            db = self.conection()
            cursor = db.cursor()
            cursor2 = db.cursor()

            #El índice donde está el usuario en el TabWidget
            index = self.tabWidget.currentIndex()
            if (index == 0):
                actualTable = self.tables_cb.currentText()
            else:                
                actualTable = self.tables_cb1.currentText()
            #Cadena para búsqueda SQL
            sqlColumns = 'show columns from {0}'.format(actualTable) #Conocer las columnas
            sqlSearch = 'select * from {0};'.formart(actualTable)                            
            cursor.execute(sqlColumns)
            cursor2.execute(sqlSearch)            
            resultado = cursor.fetchall()
            resultado2 = cursor2.fetchall()
            
            counter = 0
            self.table_insert.setRowCount(0)
            for column in resultado:
                columnName = column[0]                
                #Poner el nombre en el label de la columna
                self.table_insert.setHorizontalHeaderItem(counter).setText(columnName)
                couter += 1
            
            for fila_num, fila_dato in enumerate(resultado2):
                    self.table_insert.insertRow(fila_num)
                    for col_num, dato in enumerate(fila_dato):
                        self.table_insert.setItem(fila_num, col_num, QtWidgets.QtableWidgetItem(str(dato)))

            self.status_label.setText(self.strOK)
            cursor.close()
            cursor2.close()
        except:
            self.status_label.setText(self.strError)
        finally:
            db.close()

    #def fn_insert(self):


            


def main():    
    app = QApplication(sys.argv)
    GUI = Db_GUI()
    GUI.show()
    sys.exit(app.exec_())   

if __name__ == "__main__":
    main()