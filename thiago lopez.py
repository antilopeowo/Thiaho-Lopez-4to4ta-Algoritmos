import random


def ejercicio1():
    CantidadActual = 1000
    BalatroBalatrez = True
    while BalatroBalatrez:
        try:
            print(f"""
                Banco "El Balatro"
                Saldo Actual:{CantidadActual}

                1)Retirar chips y multi
                2)Depositar chips y multi
                3)ser vencido por el balatro (salir)
            """)
            op = int(input("elija su opcion:"))
            if op == 1:
                CantidadRetirada = int(input("Elija la cantidad a retirar:"))
                if CantidadRetirada <= CantidadActual:
                    CantidadActual -= CantidadRetirada
            if op == 2:
                CantidadDepositada = int(input("ingrese la cantidad a depositar"))
                CantidadActual += CantidadDepositada
            if op == 3:
                print("fue humillado por el balatro")
                BalatroBalatrez = False
        except ValueError:
            BalatroBalatrez = True
            print("Error, fue vencido por el balatro involuntariamente")


def ejercicio2():
    WHILE = True
    while WHILE:
        try:
            print("""
            Calculadora de gordofobia

            1)Calcular
            2)Salir
            """)
            op = int(input("ingrese su opcion"))
            if op == 2:
                WHILE = False
                print("Cerrando programa")
            elif op == 1:
                Peso = float(input("ingrese su peso:"))
                Altura = float(input("ingrese su Altura:"))
                AlturaM = Altura * Altura
                IMC = Peso / AlturaM
                if IMC <= 18.0:
                    print(f"estas muy flaco{IMC}")
                elif IMC <= 24.9:
                    print(f"estas finisimo chaval{IMC}")
                elif IMC >= 25:
                    print(f"estas gordo wanchope{IMC}")
        except ValueError:
            print("error elija la opcion de nuevo")


def ejercicio3():
    vocales = ["a", "e", "i", "o", "u"]
    seguimos = True
    while seguimos:
        try:
            frase = input("Ingrese una Frase: ")
            if frase == "agusfortnite2008":
                print("Nooo todo menos esoo")
                seguimos = False
            else:
                for vocales_a_buscar in range(0, len(vocales) - 1):
                    vocal_aleatoria = random.randint(0, 4)
                    frase = frase.replace(vocales[vocales_a_buscar], vocales[vocal_aleatoria])
                print(frase)
        except ValueError:
            print("Valor Inválido, Inténtelo de Nuevo: ")
def ejercicio4():
    seguimos = True
    frase_invertida = ""
    while seguimos:
        palabras_separadas = []
        frase = input("ingrese una frase: ")
        palabras_separadas = frase.split()
        print(palabras_separadas)
        for x in range(0, len(palabras_separadas)):
            palabras_separadas[x] = palabras_separadas[x][::-1]
        frase_invertida += " ".join(palabras_separadas)
        print(frase_invertida)
def ejercicio5():
    Lista_Nombres = []
    Seguimos = True

    while Seguimos:
        try:
            Ingreso_Usuario = int(input("""
                
                1. Ingresar alumno en lista
                2. Ver Alumno
                3. Salir
            """))
            if Ingreso_Usuario == 1:
               Nombre_a_Ingresar=input("Ingrese un nombre")
               Lista_Nombres.append(Nombre_a_Ingresar)
               Seguimos = True
            elif Ingreso_Usuario == 2:
                print("Lista de Alumnos", Lista_Nombres)
                Ver_Alumno = int(input("Ingrese indice de alumno"))
                print(Lista_Nombres[Ver_Alumno-1 ])
                Seguimos = True
            elif Ingreso_Usuario == 3:
               print("chau")
               Seguimos = False
        except ValueError:
            print("Tipo de dato ingresado incorrecto")
        except IndexError:
            print("Indice de la lista no disponible")

ejercicio5()