# Ejercicio: Suma de Múltiplos de 3 o 5
def suma_multiplos(lista):
    #Le damos un valor de 0 a la suma
    suma = 0
    #Hacemos un for para recorrer la lista
    for numero in lista:
        #Si el número es múltiplo de 3 o 5, lo sumamos a la variable suma
        if numero % 3 == 0 or numero % 5 == 0:
            suma += numero
    #Retornamos suma
    return suma

# Ejemplo de uso:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
resultado = suma_multiplos(numeros)
print(f"La suma de los múltiplos de 3 o 5 en la lista es: {resultado}")
