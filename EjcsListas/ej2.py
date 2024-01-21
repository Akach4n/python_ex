#Ordenar pares e impares
def ordenar_pares_impares(lista):
    #Creamos dos listas vacías de pares e impares
    pares = []
    impares = []
    #Recorremos la lista
    for numero in lista:
        #Si el número es par hacemos lo siguiente
        if numero % 2 == 0:
            #Añadimos con .append al array "pares" la variable número cada vez que se cumpla el if
            pares.append(numero)
        else:
            #Añadimos con .append al array "impares" la variable número cada vez que no se cumpla el if
            impares.append(numero) 
    #Juntamos los dos arrays en uno mismo con .extend        
    pares.extend(impares)
    return pares

# Ejemplo de uso:
numeros = [7, 2, 5, 8, 1, 3, 10, 6, 4, 9]
resultado = ordenar_pares_impares(numeros)
print(f"Lista original: {numeros}")
print(f"Lista ordenada con pares primero e impares después: {resultado}")
