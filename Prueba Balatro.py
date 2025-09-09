def crear_matriz():
    baraja=[]
    carta=[]
    palos=["Espada","Corazon"," Trebol","Diamante"]
    for l in range(0, len(palos)):
        for x in range(1, 14):
            if x==11:
                x="J"
            elif x==12:
                x="Q"
            elif x==13:
                x="K"
            elif x==1:
                x="A"
            carta.append(x)
            carta.append(palos[l])
            baraja.append(carta)
            carta=[]
    return baraja

def sumar(matriz):
    suma=0
    for x in range(0, len(matriz)):
        if matriz[x][0] == "A":
            suma += 11
        elif matriz[x][0] == "J" or matriz[x][0] == "Q" or matriz[x][0] == "K":
            suma += 10
        else:
            suma += matriz[x][0]
    print(suma)
sumar(crear_matriz())