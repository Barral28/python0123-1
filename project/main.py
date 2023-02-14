import controller as ctr
import pandas as pd

message="""
    1) Insertar un usuario
    2) Mostrar de usuarios
    3) Eliminar usuario
    4) Actualizar usuario
    5) Salir
"""
global opc

def registerUser():
    usuario=input("Data usuario: ")
    password=input("Password: ")
    email=input("Email: ")
    fullname=input("Nombre completo: ")
    tipousuario=input("Tipo de usuario: ")
    data=(usuario,password,email,fullname,tipousuario)
    try:
        ctr.insertUser(data)
    except Exception as e:
         print("Error")
         print(e)

def listUser():
    data=ctr.controllerUser()
    for row in data:
        print(row)
   
    key_list=['ID','USUARIO','CONTRASEÑA','EMAIL','NOMBRE COMPLETO','SCORE','TIPO USUARIO']
    df=pd.DataFrame(data, columns=key_list)
    print(df)

def deleteUser():
    id = int(input("Ingrese el numero de ID: "))
    data = (id,)
    try:
        ctr.deleteUser(data)
    except Exception as e:
         print("Error")
         print(e)

def updateUser():
    id = int(input("ID:: "))
    usuario=input("Data usuario: ")
    password=input("Password: ")
    email=input("Email: ")
    full_name=input("Nombre completo: ")
    score  =int(input("Score:"))
    tipo_usuario=input("Tipo de usuario: ")
    data = (usuario,password,email,full_name,score,tipo_usuario,id)
    
    try:
        ctr.updateUser(data)
    except Exception as e:
         print("Error")
         print(e)

if __name__=='__main__':
    while True:
        print(message)
        opc=input('ingrese una opcion: ')
        if opc=='1':
            registerUser()
        elif opc == '2':
            listUser()
        elif opc == '3':
            deleteUser()
        elif opc == '4':
            updateUser()
        elif opc=='5':
            print("Gracias por usar la aplicacion, buen viaje")
            break
        else:
            print("Opcion invalida")
            break
