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

class Jugador:
    '''Representa a un jugador de loba.'''
    #constructor
    def __init__(self,nombre,puntos,total):
        self.nombre = nombre
        self.puntos = puntos
        self.total = total

j = 0
k = 0
jugadores = {}

while j  != cont:
    for nombre in nombres:
        jugadores.update({nombre: Jugador(nombre,[],0)})
        j = j + 1

print(jugadores)