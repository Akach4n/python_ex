#Encontrar números duplicados
def encontrar_duplicados(lista):
    # duplicados = []
    # numeros_vistos = set()
    # lista_final = []
    # for numero in lista:
    #     if numero in numeros_vistos:
    #         duplicados.append(numero)
    #     else:
    #         numeros_vistos.add(numero)
    #         lista_final.append(numero)
    lista_final = set()
    for numero in lista:
        lista_final.add(numero)


    return lista_final

# Ejemplo de uso:
numeros = [1, 2, 3, 4, 5, 2, 6, 7, 8, 9, 10, 4]
duplicados = encontrar_duplicados(numeros)
print(f"Lista original: {numeros}")
print(f"Elementos duplicados: {duplicados}")
