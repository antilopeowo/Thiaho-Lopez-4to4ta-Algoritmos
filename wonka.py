import random
def ejercicio1():
    precio=int(input("indique el precio de su producto:"))
    if precio>=100:
        descuento=precio*0.15
        precio_final=precio-descuento
        print(f"su precio con el descuento del 15% es:{precio_final} y su descuento es {descuento}%")
    elif precio>=99.99 and precio>=50:
        descuento = precio * 0.10
        precio_final = precio - descuento
        print(f"su precio con el descuento del 10% es:{precio_final} y su descuento es {descuento}%")
    elif precio<50:
        print(f"no hay descuento {precio}")
def ejercicio2():
    ola=True
    num_secreto = []
    num_secreto.append(random.randint(0, 10))
    while ola:
        print(num_secreto)
        usuario = int(input("ingrese el numero secreto:"))
        for x in range(len(num_secreto)):
            if usuario>num_secreto[x]:
                print("no adivinaste el numero, el numero ingresado es mas grande que el secreto")
            elif usuario<num_secreto[x]:
                print("no adivinaste el numero, el numero ingresado es mas pequeño que el secreto")
            if usuario==num_secreto[x]:
                print("adivinaste el numero")
                ola=False
def ejercicio3():
    vocl = ["á", "é", "í", "ó", "ú", "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    list1 = []
    list2 = []
    cont = 0
    palabra = input("ingrese una palabra")
    for letra in palabra:
        if letra in vocl:
            cont = cont + 1
            list2.append(letra)
    print(f"En la palabra {palabra} estan {list2} como vocales {cont}")
def ejercicio4():
    num=int(input("ingrese un numero:"))
    for num in range(num, num*10+1, num):
        print(num)
def ejercicio5():
    ola=True
    aux = 0
    while ola:
        jose=int(input("ingrese numeros:"))
        if jose%2==0:
            aux=aux+jose

        if jose==0:
            ola=False
        print(aux)
