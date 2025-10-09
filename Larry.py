def ejercicio1():
   productos = [
       {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica"},
       {"nombre": "Mouse", "precio": 25, "categoria": "Electrónica"},
       {"nombre": "Teclado", "precio": 75, "categoria": "Electrónica"},
       {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}
   ]
   for pene in productos:
       print(pene["nombre"])
def ejercicio2():
   productos = [
       {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica"},
       {"nombre": "Mouse", "precio": 25, "categoria": "Electrónica"},
       {"nombre": "Teclado", "precio": 75, "categoria": "Electrónica"},
       {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}
   ]
   precio1=productos[0]["precio"]
   precio2=productos[1]["precio"]
   precio3=productos[2]["precio"]
   precio4=productos[3]["precio"]
   suma=precio4+precio3+precio2+precio1
   print(suma)
def ejercicio3():
   productos = [
       {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica"},
       {"nombre": "Mouse", "precio": 25, "categoria": "Electrónica"},
       {"nombre": "Teclado", "precio": 75, "categoria": "Electrónica"},
       {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}
   ]
   productos.append("teto")
def ejercicio4():
   productos = [
       {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica"},
       {"nombre": "Mouse", "precio": 25, "categoria": "Electrónica"},
       {"nombre": "Teclado", "precio": 75, "categoria": "Electrónica"},
       {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}
   ]
   productos[0]["precio"]="diemildolal"
def ejercicio5():
   estudiantes = [
   {"nombre": "Ana", "edad": 21, "calificacion": 90},
   {"nombre": "Luis", "edad": 22, "calificacion": 95},
   {"nombre": "Marta", "edad": 20, "calificacion": 85}
   ]
   ola=[0]
   for penerico in estudiantes:
       if penerico["calificacion"]>=ola[0]:
           ola[0]=penerico["calificacion"]
   print(ola)
def ejercicio6():
   estudiantes = [
       {"nombre": "Ana", "edad": 21, "calificacion": 90},
       {"nombre": "Luis", "edad": 22, "calificacion": 95},
       {"nombre": "Marta", "edad": 20, "calificacion": 85}
   ]
   estudiantes_labubusificados=[]
   for bruh in estudiantes:
       estudiantes_labubusificados.append(bruh["nombre"])
   print(estudiantes_labubusificados)
def ejercicio7():
   libros = [
       {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez"},
       {"titulo": "Don Quijote", "autor": "Miguel de Cervantes"},
       {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón"}
   ]
   ola=libros[1]
   libros.remove(ola)
   libros.append(ola)
def ejercicio8():
   libros = [
       {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez"},
       {"titulo": "Don Quijote", "autor": "Miguel de Cervantes"},
       {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón"}
   ]
   for libro in libros:
       libro["disponible"]=True
   print(libros)
ejercicio8()
