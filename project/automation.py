import pandas as pd
import os
import db

def insertData():
    compra = float(input("Ingrese data de  compra: "))
    venta = float(input("Ingrese data de  venta: "))
    fecha = input("Ingrese la fecha: ")
    data = (compra,venta,fecha)
    query="INSERT INTO CAMBIO_DOLAR VALUES(NULL,?,?,?)"
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()
    cursor.execute(query,data).fetchall()
    conn.con.commit()
    print("Datos insertados")


def readData():
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()
    query="SELECT * FROM VENTA_COMPRA"
    result = cursor.execute(query).fetchall()
    key_list=['ID','COMPRA DOLAR','VENTA DOLAR','FECHA']
    df=pd.DataFrame(result,columns=key_list)
    print(df)
    print("desea generar un reporte ?")
    a=input("Elija una de las opciones: (Si/No): ")
    if (a.lower() =='si'):
        df.to_excel('Reporte_precio_Dolar.xlsx',sheet_name='reporte',index=False)
    elif(a.lower() =='no'):
        print("Muchas gracias por usar la aplicacion , que tenga buen dia")
    else:
        print("Error")

def updateData():
    id = int(input("Ingrese ID: "))
    if(id > 0):
        compra = float(input("Ingrese valor compra:"))
        venta = float(input("Ingrese valor venta:"))
        fecha = input("Ingrese la  fecha:")
        data = (compra,venta,fecha,id)
        query="UPDATE VENTA_COMPRA SET COMPRA=?,VENTA=?,FECHA =? WHERE ID = ? "
        conn=db.Conection('tienda.db')
        cursor=conn.getCursor()
        result=cursor.execute(query,data).fetchall()
        conn.con.commit()
        print("Cambios actualizados")
        # print(result)
    else:
        print("Error")
        
while True:
    try:
        message="""
            1) Insertar datos:
            2) Actualizar data dolar
            3) Salir
            """
        print(message)
        opc=int(input('ingrese la tarea a realizar: '))
        if(opc==1):
            insertData()
            readData()
        elif(opc==2):
            updateData()
            readData()
        elif(opc==3):
            print("Gracias por usar la aplicacion, buen viaje")
            break
        else:
            break
    except Exception as e:
         print("Error")
         print(e)
    