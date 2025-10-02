def ejercicio1():
    informacion_personal={
        "nombre":"Thiago Lopez",
        "edad":16,
        "ciudad":"La matanza",
        "Trabajo":"abastecedor logistico en lugares de alta concentracion"
    }
    print(informacion_personal)
def ejercicio2():
    informacion_personal = {
        "nombre": "Thiago Lopez",
        "edad": 16,
        "ciudad": "La matanza",
        "Trabajo": "abastecedor logistico en lugares de alta concentracion",
        "telefono":1140978500,
        "email":"pepitorogelioalbertojuanespeciedelos8montespicudosdesanmarateadelbarrrancojose@gmail.com"
    }
    informacion_personal["ciudad"]="Carapegua"
    informacion_personal["Trabajo"]="vendedor de chipa"
def ejercicio3():
    Materias={
        "Matematica":10,
        "Algoritmos":9,
        "Lengua":0
    }
def ejercicio4():
    Materias = {
        "Matematica": 10,
        "Algoritmos": 9,
        "Lengua": 0
    }
    math=Materias["Matematica"]
    Algoritmos=Materias["Algoritmos"]
    Lengua=Materias["Lengua"]
    suma=math+Algoritmos+Lengua
    promedio=suma/3
    print(promedio)
def ejercicio5():
    paises_capitales={
        "Argentina":"Buenos Aires",
        "Alemania":"Berlin",
        "Ucrania":"Kiev",
        "Paraguay":"Asuncion"
    }
    usuario=input("Ingrese un país:")
    print(f"Su capital es: {paises_capitales[usuario]}")
def ejercicio6():
    Productos={
        "Harina":2,
        "Flan":3,
        "Yogurt":2.5
    }
    producto=input("ingrese el nombre del producto:")
    cantidad=int(input("ingrese su cantidad:"))
    idk=Productos[producto]*cantidad
    print(f"el precio de los productos es: ${idk}")
def ejercicio7():
    informacion_personal = {
        "nombre": "Thiago Lopez",
        "edad": 16,
        "ciudad": "La matanza",
        "Trabajo": "abastecedor logistico en lugares de alta concentracion",
        "telefono": 1140978500,
        "email": "pepitorogelioalbertojuanespeciedelos8montespicudosdesanmarateadelbarrrancojose@gmail.com"
    }
    del informacion_personal["telefono"]
    print(informacion_personal)
def ejercicio8():
    informacion_personal = {
        "nombre": "Thiago Lopez",
        "edad": 16,
        "ciudad": "La matanza",
        "Trabajo": "abastecedor logistico en lugares de alta concentracion",
        "telefono": 1140978500,
        "email": "pepitorogelioalbertojuanespeciedelos8montespicudosdesanmarateadelbarrrancojose@gmail.com"
    }
    clave=input("ingrese una clave")
    if clave in informacion_personal:
        print("True")
    else:
        print("False")
def combinando_diccionarios():
    jugadores={
        "Jugador1": "Lionel Messi",
        "jugador2": "Kylian Mbappe",
        "jugador3": "Erling Haañamd",
        "jugador4": "Vinicius Junior"
    }
    equipos={
        "equipo1":"Inter Miami CF",
        "equipo2": "Real Madrid",
        "equipo3": "Manchester city",
        "equipo4": "Real Madrid"
    }
    jugadores_y_equipos=jugadores|equipos
    print(jugadores_y_equipos)
