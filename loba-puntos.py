'''Programa que lleva la cuenta de los puntos de la Loba.
Se puede definir el número de jugadores y 3 modalidades de juego para que finalice la partida de 
manera automática.'''

nombres = []
i = 0
cont = int(input("ingresar cantidad de jugadores: "))

while i != cont:
    for i in range(0,cont):
        valor = input("ingrese un nombre: ").capitalize()
        nombres.append(valor)
        i = i + 1
print(nombres)

jugadores = {}
j = 0

for j in range(0,len(nombres)):
    jugadores.update({nombres[j] : {}})
    j = j + 1
print(jugadores)

for elemento in jugadores:
    jugadores[elemento].update({'puntos':[]})
print(jugadores)