''' 1) Escribir una función que calcule el máximo común divisor entre dos números. '''

def mcd(x, y):
    mcd = 1 
    
    if x % y == 0:
        return y
    
    
    for variable in range(int(y/2), 0, -1):
        if x % variable == 0 and y % variable == 0:
            mcd = variable
            break
        
    return mcd

print("==================================================")
print("Calculo del máximo común divisor entre dos números")
print("==================================================")


x = float(input("Ingrese un numero: "))
y = float(input("Ingrese otro numero: "))

Máximocd = mcd(x, y)

print(f"El máximo común divisor entre los dos números es: {Máximocd}")