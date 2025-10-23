def ejercicio1():
    matriz=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    for x in range(0, len(matriz)):
        print(matriz[x])
def ejercicio2():
    matriz=[
        [10,20,30],
        [40,50,60],
        [70,80,90]
    ]
    aux=0
    for x in range(0, len(matriz)):
        for y in range(0, len(matriz[x])):
            aux+=matriz[x][y]
    print(aux)
def ejercicio3():
    matriz=[
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]
    print(matriz)
    indice_fila=int(input("ingrese su indice de fila"))
    indice_columna=int(input("ingrese su indice de columna"))
    print(matriz[indice_fila][indice_columna])
def ejercicio4():
    matriz = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    aux=0
    for x in range(0,len(matriz)):
        for y in range(0, len(matriz[x])):
            if aux<matriz[x][y]:
                aux=matriz[x][y]
                print(aux)
ejercicio4()