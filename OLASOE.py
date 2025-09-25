pepe=True
matriz = [
   [0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]

]
while pepe:
   casilla=int(input("ingrese un numero de casilla"))
   casilla2=int(input("ingrese otra casilla"))
   jugador=input("ingrese que jugador eres (x , o):")
   if jugador=="o":
       
   elif jugador=="x":
   if jugador=="x" or jugador == "X":
       matriz[casilla][casilla2] = "X"
   elif jugador == "o" or jugador == "O":
       matriz[casilla][casilla2] = "O"
   if matriz[0][0]==matriz[1][1]==matriz[2][2]:

               print("gano o")

   print(matriz)