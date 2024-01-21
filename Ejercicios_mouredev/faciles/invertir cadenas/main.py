def invertir_cadena(cadena):
    cadena_invertida = ""
    for i in range(len(cadena) -1, -1, -1):
        cadena_invertida += cadena[i]
    return cadena_invertida

texto = str(input("Escribe algún texto para invertirlo:\n"))

print(invertir_cadena(texto)) 