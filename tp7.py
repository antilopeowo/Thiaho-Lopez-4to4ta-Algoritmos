import mysql.connector
from mysql.connector import errorcode
import datetime

cursor = None
cnx = None


def conectarBase():
    global cnx, cursor
    try:
        cnx = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="rubricas_db"
        )
        cursor = cnx.cursor(dictionary=True)
        print("conexión establecida")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("usuario o contraseña incorrectos")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("la base de datos no existe")
        else:
            print(err)

conectarBase()



def consultaSelect(tabla):
    Consulta = f"SELECT * FROM {tabla};"
    cursor.execute(Consulta)
    return cursor.fetchall()



def agregarRubrica():
    nombre = input("ingrese el nombre de la rúbrica: ")

    sql = "INSERT INTO rubricas (nombre) VALUES (%s)"
    cursor.execute(sql, (nombre,))
    cnx.commit()

    rubrica_id = cursor.lastrowid
    print(f"rúbrica creada con ID {rubrica_id}")

    agregarCriterios(rubrica_id)


def agregarCriterios(rubrica_id):
    print("\n ingrese criterios para esta rúbrica")
    print("escriba 'fin' para dejar de agregar\n")

    while True:
        nombre = input("nombre del criterio: ").strip()

        if nombre.lower() == "fin":
            print("criterios fueron cargados")
            break

        puntaje = int(input("puntaje máximo del criterio: "))

        sql = """
            INSERT INTO criterios (rubrica_id, nombre, puntaje_max)
            VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (rubrica_id, nombre, puntaje))
        cnx.commit()

        print("criterio agregado \n")



def mostrarRubricas():
    rubricas = consultaSelect("rubricas")

    if not rubricas:
        print("sin rubricas registradas")
        return None

    print("\n lista de rubricas")
    for rub in rubricas:
        print(f"{rub['id']}) {rub['nombre']}")

    return rubricas



def mostrarRubricaCompleta():
    rubricas = mostrarRubricas()
    if not rubricas:
        return

    elegido = int(input("\nIngrese el ID de la rúbrica que desea ver: "))

    cursor.execute("SELECT * FROM rubricas WHERE id=%s", (elegido,))
    rubrica = cursor.fetchone()

    if not rubrica:
        print("ID inválido")
        return

    print(f"\n=== {rubrica['nombre']} ===")


    cursor.execute("SELECT * FROM criterios WHERE rubrica_id=%s", (elegido,))
    criterios = cursor.fetchall()

    if not criterios:
        print("Esta rúbrica esta sin criterios")
        return

    for c in criterios:
        print(f"- {c['nombre']} (máx {c['puntaje_max']})")



def menu():
    while True:
        opcion = int(input("""
===========================
     MENÚ DE RÚBRICAS
===========================
1) Crear nueva rúbrica
2) Mostrar todas las rúbricas
3) Mostrar rúbrica completa
4) Salir
Ingrese opción: """))

        if opcion == 1:
            agregarRubrica()

        elif opcion == 2:
            mostrarRubricas()

        elif opcion == 3:
            mostrarRubricaCompleta()

        elif opcion == 4:
            print("saliendo")
            break

        else:
            print("esta opcion esta invalida")


menu()