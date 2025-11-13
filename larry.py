import mysql.connector
import json
import datetime


cnx = None
cursor = None




def Conectar():
  global cnx, cursor
  cnx = mysql.connector.connect(user="root", password="", host="Localhost", database="holi")
  cursor = cnx.cursor(dictionary=True)
  print('Conexión establecida')




def ConsultaSelect():
  Consulta = "SELECT * FROM clientes;"
  cursor.execute(Consulta)
  return cursor.fetchall()




def ConsultaInsertar(nombre, dni, correo, saldo):
  sql = "INSERT INTO clientes (nombre, dni, correo, saldo) VALUES ( %s, %s, %s, %s)"
  cursor.execute(sql, (nombre, dni, correo, saldo))
  cnx.commit()
  return cursor.lastrowid


Conectar()


resultado = ConsultaSelect()


for x in resultado:
  print(x)


Conectar()


def ejercicio2():
  resultado = str(ConsultaSelect())
  nombre_archivo = "datos_usuario.json"
  with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
      json.dump(resultado, archivo, indent=4, ensure_ascii=False)
def ejercicio4():
  ConsultaSelect()
  Consulta = "UPDATE clientes set nombre='Travesti' WHERE id = 1;"
  cursor.execute(Consulta)
  cnx.commit()
  return cursor.fetchall()
def insertar_cliente(nombre,dni,correo,saldo):
   sql = "INSERT INTO clientes (nombre, dni, correo, saldo)VALUES( %s, %s, %s, %s)"
   cursor.execute(sql, (nombre, dni, correo, saldo))
   cnx.commit()
   return cursor.lastrowid




def ejercicio5():
   insertar1 = int(input("1- cliente"
                         "2- pagos"
                         "3- pedidos"
                         "4- productos"))


   if insertar1 == 1:
       nombre = input("Ingrese el nombre: ")
       dni = input("Ingrese el DNI: ")
       correo = input("Ingrese el correo: ")
       saldo = int(input("Ingrese el saldo: "))
       insertar_cliente(nombre, dni, correo, saldo)
   elif insertar1 == 2:
       nombre = input("Ingrese el nombre: ")
       categoria = input("Ingrese la categoria: ")
       precio = input("Ingrese el precio: ")
       stock = int(input("Ingrese el stock: "))
       insertar_pagos(nombre, categoria, precio, stock)
   elif insertar1 == 3:
       pedido_id = int(input("Ingrese el id el pedido: "))
       monto = int(input("Ingrese el monto: "))
       fecha = datetime.date(int(input("ingrese el año")), int(input("ingrese el mes")), int(input("ingrese el dia")))
       insertar_pedidos(pedido_id, monto, fecha)
   elif insertar1 == 4:
       cliente_id = int(input("Ingrese el id del cliente: "))
       fecha = datetime.date(int(input("ingrese el año")), int(input("ingrese el mes")), int(input("ingrese el dia")))
       total = int(input("Ingrese el total: "))
       insertar_producto(cliente_id, fecha, total)


def insertar_producto(nombre, categoria, precio, stock):
    sql = "INSERT INTO productos (id, nombre, categoria, precio, stock)VALUES( %s, %s, %s, %s, %s)"
    cursor.execute(sql, (nombre, categoria, precio, stock))
    cnx.commit()
    return cursor.lastrowid
def insertar_pagos(pedido_id, monto, fecha):
    sql = "INSERT INTO pagos (pedido_id, monto, fecha)VALUES( %s, %s, %s)"
    cursor.execute(sql, (pedido_id, monto, fecha))
    cnx.commit()
    return cursor.lastrowid
def insertar_pedidos(cliente_id, fecha, total):
    sql = "INSERT INTO pedidos (cliente_id, fecha, total)VALUES( %s, %s, %s)"
    cursor.execute(sql, (cliente_id, fecha, total))
    cnx.commit()
    return cursor.lastrowid
ejercicio5()
def ejercicio6():
    print("""
        
        1)ej1
        2)ej2
        3)ej3
        4)ej4
        5)ej5    
    """)
    teto=int(input("ingrese una opcion:"))
    if teto==1:
        ConsultaInsertar()
    elif teto==2:
        ejercicio2()
    elif teto==3:
        insertar_cliente()
    elif teto==4:
        ejercicio4()
    elif teto==5:
        ejercicio5()
