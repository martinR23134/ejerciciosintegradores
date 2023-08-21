''' 2) Escribir una función que calcule el mínimo común múltiplo entre dos números '''

def mcm(x, y):
    f = max(x, y)
    
    while True:
        if (f % x == 0) and (f % y == 0):
            return f
        
        f += 1
        
print("==================================================")
print("Calculo del mínimo común divisor entre dos números")
print("==================================================")


x = float(input("Ingrese un numero: "))
y = float(input("Ingrese otro numero: "))

Mínimod = mcm(x, y)

print(f"El mínimo común divisor entre los dos números es: {Mínimod}")