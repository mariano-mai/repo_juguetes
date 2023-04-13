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
'''i = 0
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

print(jug)'''

#clase Jugador
'''class Jugador:
    'Representa a un jugador de loba.'
    #constructor
    def __init__(self,nombre,puntos,total):
        self.nombre = nombre
        self.puntos = puntos
        self.total = total
    
    #métodos
    def puntuar(self):
        'añade valores a un lista y los suma'
        numeros = []
        i = 0
        suma = 0
        #cont = int(input("ingresar cantidad de valores: ")) #temporal, se va a definir fuera del método

        while suma < 100:
            #for i in range(0,cont):
            valor = int(input("ingrese un número: "))
            numeros.append(valor)
            suma = suma + valor
            #i = i + 1
            for numero in numeros:
                print(numero)
            print("<",suma,">")

jugador1 = Jugador("Mariano", [], 0)
#jugador2 = Jugador("Agustín", [], 0)

jugador1.puntuar()
#jugador2.puntuar()'''

#recorrer un diccionario
dicc = {
    'clave1' : {
        "nombre" : "Mariano",
        "puntos" : [],
        "total" : 0
    },
    'clave2' : {
        "nombre" : "Agustín",
        "puntos" : [],
        "total" : 0
    },
    'clave3' : {
        "nombre" : "Francisco",
        "puntos" : [],
        "total" : 0
    }
}

for key in dicc:
    print(key)