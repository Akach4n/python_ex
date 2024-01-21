#Duplicar Números Pares
def duplicar_pares(lista):
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            numero *= 2
            pares.append(numero)
        else:
            impares.append(numero)
    pares.extend(impares)
    return pares

# Ejemplo de uso:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = duplicar_pares(numeros)
print(f"Lista original: {numeros}")
print(f"Lista con números pares duplicados: {resultado}")
