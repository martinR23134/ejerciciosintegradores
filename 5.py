''' 5) Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva.
'''

def get_int():
    while True:
        try:
            valor = int(input("Ingrese un valor entero: "))
            return valor
        except ValueError:
            print("Valor no válido! Intente nuevamente.")


entero = get_int()
print(f"El valor entero ingresado es: {entero}")


def get_int():
    try:
        valor = int(input("Ingrese un valor entero: "))
        return valor
    except ValueError:
        print("Valor no válido! Intente nuevamente.")
        return get_int()


entero = get_int()
print(f"El valor entero ingresado es: {entero}")