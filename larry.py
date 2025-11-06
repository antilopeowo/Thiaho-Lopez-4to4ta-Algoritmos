matriz=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
lista=[]
for x in range(0,len(matriz)):
    for y in range(0,len(matriz[x])):
        lista.append(matriz[x][y])
print(lista)