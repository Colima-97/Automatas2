import sys
import pymysql
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidget, QTableWidgetItem

class Db_GUI(QMainWindow):
   

    def __init__(self):
        super().__init__()
        uic.loadUi("myGUI.ui", self)
        #Defining variables and flags
        self.strError = 'Ocurrió un error'
        self.strOK = 'Todo marcha sobre ruedas'
        self.comboBox1Flag = False #It means that comboBox1 hasn't been filled
        self.comboBox2Flag = False #It means that comboBox2 hasn't been filled        
        #Filling comboBox        
        self.fn_comboBox_fill()      
        #Listeners for changes  
        self.tabWidget.currentChanged.connect(self.fn_comboBox_fill)
        self.tables_cb1.currentIndexChanged.connect(self.fn_showInsertColumns)
        #Firstly operations
        self.tabWidget.setCurrentIndex(0)
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

                self.fn_showInsertColumns()                 
            else:
                print('It has been already filled!')

    def fn_show(self):
        try:
            db = self.conection()
            cursor = db.cursor()
            cursor2 = db.cursor()
             
            #SQL Queries
            actualTable = self.tables_cb.currentText()
            sqlColumns = 'show columns from {0}'.format(actualTable) #Knowing the columns' name
            sqlSearch = 'select * from {0};'.format(actualTable)                            
            cursor.execute(sqlColumns)
            cursor2.execute(sqlSearch)            
            resultado = cursor.fetchall()
            resultado2 = cursor2.fetchall()

            #Num of columns
            lon = (len(resultado))
            self.table_show.setRowCount(0)
            self.table_show.setColumnCount(lon)
            column_array = []
            for column in resultado:
                columnName = column[0]                
                #Adding the name of the column into an array
                column_array.append(columnName)                
            #Setting all columns with an array
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

    def fn_showInsertColumns(self):
        try:
            db = self.conection()
            cursor = db.cursor()

            #SQL Queries
            actualTable = self.tables_cb1.currentText()
            sqlColumns = 'show columns from {0}'.format(actualTable) #Knowing the columns' name
            
            cursor.execute(sqlColumns)
            resultado = cursor.fetchall()

            #Num of columns
            lon = (len(resultado))
            self.table_insert.setRowCount(1)
            self.table_insert.setColumnCount(lon)
            column_array = []
            for column in resultado:
                columnName = column[0]                
                #Adding the name of the column into an array
                column_array.append(columnName)                
            #Setting all columns with an array
            self.table_insert.setHorizontalHeaderLabels(column_array)

            self.status_label.setText(self.strOK)
            cursor.close()
        except:
            self.status_label.setText(self.strError)
        finally:
            db.close()



            


def main():    
    app = QApplication(sys.argv)
    GUI = Db_GUI()
    GUI.show()
    sys.exit(app.exec_())   

if __name__ == "__main__":
    main()