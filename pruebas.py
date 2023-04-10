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
i = 0
j = 0
var = "Y"
suma = 0
lista = []

cont = int(input("ingresar cantidad de valores: "))

while i != cont:
    for i in range(0,cont):
        valor = int(input("ingrese un número: "))
        lista.append(valor)
        i = i + 1

for j in range(0,len(lista)):
    suma = suma + lista[j]
    j = j + 1

jug = {
    "nombre": "Mariano",
    "puntos": lista,
    "total": suma
}

jug.update({"puntos": lista})
jug.update({"total":suma})

print(jug)