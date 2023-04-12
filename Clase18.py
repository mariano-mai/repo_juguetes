#POO - programación orientada a objetos
#Ya pensar en clases.
class Persona:
    '''Documentación de la clase, puede o no estar'''

    #Constructor: define e inicializa todos los atributos
    #de la clase (getters y setters en java)
    def __init__(self,nombre, apellido, fchnac, altura, dni, peso, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.fchnac = fchnac
        self.altura = altura
        self.dni = dni
        self.peso = peso
        self.mail = mail

    #Métodos de la clase
    def hablar(self):
        print(f"Hola, soy {self.nombre}")
    
    def caminar(self):
        print(f"{self.nombre} está caminando.")

    def correr(self):
        print(f"{self.nombre} está corriendo.")

#Crear un objeto:

persona1 = Persona("Juan", "Perez", "12/10/1900", 165, 12345678, 50, "asd@gmail.com")

print(persona1.apellido)
persona1.caminar()