#Añadir valores a una lista
'''numeros = []
i = 0
cont = int(input("ingresar cantidad de valores: "))

while i != cont:
    for i in range(0,cont):
        valor = int(input("ingrese un número: "))
        numeros.append(valor)
        i = i + 1

print(numeros)'''

#Agregar elementos a un diccionario
lista = []
i = 0
j = 0
suma = 0
cont = int(input("ingresar cantidad de valores: "))

while i != cont:
    for i in range(0,cont):
        valor = int(input("ingrese un número: "))
        lista.append(valor)
        i = i + 1
#valor = int(input("ingrese un número: "))
#lista.append(valor)
while j != cont:
    for j in range(0,lista[j]):
        suma = suma + lista[j]
        print("el valor actual es: ", suma)
        j = j + 1
        print("j vale: ", j)
print("el valor total es: ", suma)

jugador = {
    "nombre" : "Mariano",
    "puntos" : lista,
}

jugador.update({"total":suma})

print(jugador)