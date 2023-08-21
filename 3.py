''' 3) Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia). '''



def contar_palabras(cadena):
    palabras = cadena.split()

    frecuencias = {}

    
    for palabra in palabras:
        palabra = palabra.lower()

        if palabra in frecuencias:
            frecuencias[palabra] += 1
   
        else:
            frecuencias[palabra] = 1

    return frecuencias


cadena = input("Ingrese una cadena de caracteres: ")

diccionario_frecuencias = contar_palabras(cadena)

for palabra, frecuencia in diccionario_frecuencias.items():
    print(f'Palabra: {palabra}, Frecuencia: {frecuencia}')