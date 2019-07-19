import sys
import pymysql
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidget, QTableWidgetItem

class Db_GUI(QMainWindow):
   

    def __init__(self):
        super().__init__()
        uic.loadUi("myGUI.ui", self)
        #Defining variables
        self.strError = 'Ocurrió un error'
        self.strOK = 'Todo marcha sobre ruedas'
        self.comboBox1Flag = False #It means that comboBox1 hasn't been filled
        self.comboBox2Flag = False #It means that comboBox1 hasn't been filled
        #Filling comboBox        
        self.fn_comboBox_fill()        
        self.tabWidget.currentChanged.connect(self.fn_comboBox_fill)
        #Buttons clicked
        self.show_btn.clicked.connect(self.fn_show)
        #self.insert_btn.clicked.connect(self.fn_insert)

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

            if(index == 0 and self.comboBox1Flag != True):
                #self.tables_cb() ComboBox 1
                self.comboBox1Flag = True
                for row in tables:
                    table = row[0]
                    self.tables_cb.addItem(table)                 
            elif (index == 1 and self.comboBox2Flag != True):
                #self.tables_cb1() ComboBox 2
                self.comboBox2Flag = True
                for row in tables:
                    table = row[0]
                    self.tables_cb1.addItem(table)                 
            else:
                print('It has been already filled!')

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
            sqlSearch = 'select * from {0};'.format(actualTable)                            
            cursor.execute(sqlColumns)
            cursor2.execute(sqlSearch)            
            resultado = cursor.fetchall()
            resultado2 = cursor2.fetchall()
            lon = (len(resultado))
            #counter = 0
            self.table_show.setRowCount(0)
            self.table_show.setColumnCount(lon)
            column_array = []
            for column in resultado:
                columnName = column[0]                
                #Poner el nombre en el label de la columna
                #self.table_insert.setHorizontalHeaderItem(counter, self.table_insert).setText(columnName)
                column_array.append(columnName)
                #couter += 1
            
            self.table_show.setHorizontalHeaderLabels(column_array)

            for fila_num, fila_dato in enumerate(resultado2):
                    self.table_show.insertRow(fila_num)
                    for col_num, dato in enumerate(fila_dato):
                        self.table_show.setItem(fila_num, col_num, QtWidgets.QTableWidgetItem(str(dato)))

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