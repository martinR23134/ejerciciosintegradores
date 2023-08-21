''' 7) Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos.
 '''
 
 
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Cuenta:
    def __init__(self):
        self.titular = self.pedir_titular()
        self.__cantidad = 0.0

    def pedir_titular(self):
        nombre = input("Ingrese el nombre del titular: ")
        return Persona(nombre)
    
    def get_cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        print(f"Titular: {self.titular.nombre}")
        print(f"Cantidad: {self.__cantidad}")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
        else:
            print("La cantidad ingresada debe ser mayor a cero.")

    def retirar(self, cantidad):
        self.__cantidad -= cantidad

cuenta = Cuenta()

cuenta.mostrar()

cantidad_ingreso = float(input("Ingrese la cantidad a ingresar: "))
cuenta.ingresar(cantidad_ingreso)

cantidad_retiro = float(input("Ingrese la cantidad a retirar: "))
cuenta.retirar(cantidad_retiro)

cuenta.mostrar()
