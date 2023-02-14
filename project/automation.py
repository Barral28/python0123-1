import pandas as pd
import os
import db
message="""
    1)Insertar data:
    2)Actualizar data del dolar
"""
print(message)
a=int(input('ingrese la tarea a realizar: '))


def insertData():
    #obtiene la ruta absoluta
    path_=os.getcwd()+'\dataTienda.csv'
    #conection a bd
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()
    print(path_)
    df = pd. read_csv (path_, sep = ";") 
    ### logica para insertar 
    for i,fila in df.iterrows():
        print(fila['ORDER_ID'])

def updateDolar():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat
    pass

message="""
    1)Insertar data
    2)Actualizar data del dolar
    3)Generar reporte [Excel]
    0)Salir
"""
print(message)
a=int(input('ingrese la tarea a realizar: '))
while a!=0:
    os.system("cls")
    if a==1:
    elif a==2:
        updateDolar()
    elif a==3:    
    else:
        print("Opcion incorrecta. Vuelva a introducir")
    print(message)
    a=int(input('ingrese la tarea a realizar: '))