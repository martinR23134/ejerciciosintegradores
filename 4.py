''' 4) Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia. '''


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

def palabra_mas_repetida(diccionario_frecuencias):
    max_palabra = None
    max_frecuencia = 0

    for palabra, frecuencia in diccionario_frecuencias.items():
        if frecuencia > max_frecuencia:
            max_palabra = palabra
            max_frecuencia = frecuencia

    return (max_palabra, max_frecuencia)


cadena = input("Ingrese una cadena de caracteres: ")

diccionario_frecuencias = contar_palabras(cadena)


palabra_repetida, frecuencia_repetida = palabra_mas_repetida(diccionario_frecuencias)


print("Diccionario de Frecuencias:")
for palabra, frecuencia in diccionario_frecuencias.items():
    print(f'Palabra: {palabra}, Frecuencia: {frecuencia}')

print(f"Palabra más repetida: {palabra_repetida}, Frecuencia: {frecuencia_repetida}")