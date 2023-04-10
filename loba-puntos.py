'''Programa que lleva la cuenta de los puntos de la Loba.
Se puede definir el número de jugadores y 3 modalidades de juego para que finalice la partida de 
manera automática.'''

nombres = []
i = 0
cont = int(input("ingresar cantidad de jugadores: "))

while i != cont:
    for i in range(0,cont):
        valor = input("ingrese un nombre: ")
        nombres.append(valor)
        i = i + 1

print(nombres)

j = 0
k = 0
jugadores = {}

while j  != cont:
    for nombre in nombres:
        jugadores.update({nombre:{}})
        j = j + 1

print(jugadores)