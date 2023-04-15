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
#print(jugadores)

for elemento in jugadores:
    jugadores[elemento].update({'puntos':[]})
    jugadores[elemento].update({'total':0})
#print(jugadores)

#lista = []

'''i = 0
lista_aux = []
while i < 3:
    for elem in jugadores:
        lista = []
        #suma = 0
        valor = int(input("ingrese un valor: "))
        lista.append(valor)
        lista_aux.extend(lista)
        jugadores[elem].update({'puntos':lista_aux})
    i = i + 1'''

#añade la cantidad determinada de valores al jugador correspondiente, siguiendo el orden del diccionario (funciona)
'''jug_nombre = int(input("ingrese condición (2): "))
for elem in jugadores:
    h = 0
    lista_aux = []
    while h < 3:
        #lista_aux = []
        if jug_nombre == 2:
            lista = []
            valor = int(input("ingrese un valor: "))
            lista.append(valor)
            lista_aux.extend(lista)
            jugadores[elem].update({'puntos':lista_aux})
        else:
            print("pasó de largo")
        h = h + 1'''

#asigna 1 (UN, singular) valor a cada jugador sin importar el orden (pregunta primero) FUNCIONA!!!
for elem in jugadores:
    lista_aux = []
    clave = input("ingrese nombre de un jugador: ").capitalize()
    lista = []
    valor = int(input("ingrese un valor: "))
    lista.append(valor)
    lista_aux.extend(lista)
    jugadores[clave].update({'puntos':lista_aux})

#no funciona, sobreescribe los valores de cada jugador
'''for elem in jugadores:
    h = 0
    #lista_aux = []
    while h < 2:
        clave = input("ingrese el nombre de un jugador: ").capitalize()
        lista = []
        lista_aux = []
        valor2 = int(input("ingrese un valor: "))
        lista.append(valor2)
        lista_aux.extend(lista)
        jugadores[clave].update({'puntos':lista_aux})
        h = h + 1'''

#esta parte es para que imprima los nombres en columnas
cadena = ""
for elem in jugadores:
    cadena = cadena + "algo"
#print(cadena)

print(jugadores)