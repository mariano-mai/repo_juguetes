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

#agrega un número determinado (2) de valores en la clave 'puntos' de cada jugador
'''t = 0
while t < 2:
    for elem in dicc:
        lista_aux = []
        lista_aux.extend(dicc[elem]['puntos'])
        lista = []
        valor = int(input("ingrese un número: "))
        lista.append(valor)
        #for i in range(len(lista)):
        lista_aux.extend(lista)
        dicc[elem].update({'puntos':lista_aux})
        valores = dicc[elem]['puntos']
        coso = dicc[elem]['nombre']
        print(coso)
        print(valores)
    t = t + 1'''

'''dix = {
    'valores' : [1,2,3,4,5,6],
    'total': 0}
suma = 0

for i in range(len(dix["valores"])):
    suma = suma + dix['valores'][i]
dix.update({'total':suma})
print(suma)
print(dix)'''

t = 0
#suma = 0
while t < 2:
    for elem in dicc:
        clave = input("ingrese clave: ")
        suma = 0
        #suma = suma + dicc[clave]['total']
        lista_aux = []
        lista_aux.extend(dicc[clave]['puntos'])
        lista = []
        valor = int(input("ingrese un número para añadir a la lista de puntos: "))
        lista.append(valor)
        lista_aux.extend(lista)
        dicc[clave].update({'puntos':lista_aux})
        for i in range(len(dicc[clave]["puntos"])):
            suma = suma + dicc[clave]['puntos'][i]
            dicc[clave].update({"total":suma})
        valores = dicc[clave]['puntos']
        coso = dicc[clave]['nombre']
        otro_coso = dicc[clave]['total']
        print(coso)
        print(valores)
        print(otro_coso)
        #print(dicc)
    t = t + 1