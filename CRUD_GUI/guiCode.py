from pymysql import cursors
import sys

#Conexión
def conection():
    try:
        #Cadena de conexión
        db = pymysql.connect("localhost","root","","mundo_peludo")
        print('Conexión exitosa!')      
    except:
        print('La conexión falló!')
    finally:
        print(db)


def main():
    #conection()
    
    #sys.path.append('C:\\Users\\rap_p\\AppData\\local\\programs\\Python\\Python37-32\\lib\\site-packages')
    #sys.path.append('C:\\Users\\rap_p\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\PyMySQL-0.9.3.dist-info')
    print(sys.path)

if __name__ == "__main__":
    main()