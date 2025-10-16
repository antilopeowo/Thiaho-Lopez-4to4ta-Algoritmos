import random
suma=0
clima=[]
aux=0
indice=0
for x in range(1, 31):
    temperatura = random.randint(0, 40)
    clima.append(temperatura)
for t in range(0, len(clima)):
    suma = suma + clima[t]
    if clima[t]>aux:
        indice = t+1
        aux=clima[t]
    if clima[t] < aux:
        indice = t + 1
        aux = clima[t]
    if clima[t]>=26:
        print(f"hace calor.{clima[t]}")
    elif clima[t]<=16:
        print(f"hace frio.{clima[t]}")
    else:
        print(f"esta estable.{clima[t]}")
promedio=suma/len(clima)
print(f"el dia con mayor temperatura es el:{indice} con {aux}")
print(promedio)
