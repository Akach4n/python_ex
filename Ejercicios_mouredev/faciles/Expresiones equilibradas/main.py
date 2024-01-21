def cadenas(cadena1: str, cadena2: str):
    # Inicializar una lista para almacenar caracteres presentes en cadena1 pero no en cadena2
    char_no_comunes_str1 = []

    # Iterar sobre cada caracter en cadena1
    for char1 in cadena1:
        # Verificar si el caracter no está presente en cadena2
        if char1 not in cadena2:
            # Si no está presente, agregarlo a la lista
            char_no_comunes_str1.append(char1)

    # Unir los caracteres de la lista en una cadena
    out1 = ''.join(char_no_comunes_str1)

    # Inicializar una lista para almacenar caracteres presentes en cadena2 pero no en cadena1
    char_no_comunes_str2 = []       

    # Iterar sobre cada caracter en cadena2
    for char2 in cadena2:
        # Verificar si el caracter no está presente en cadena1
        if char2 not in cadena1:
            # Si no está presente, agregarlo a la lista
            char_no_comunes_str2.append(char2)

    # Unir los caracteres de la lista en una cadena
    out2 = ''.join(char_no_comunes_str2)

    # Imprimir los resultados
    print(f"Caracteres en str1 pero no en str2: {out1}")
    print(f"Caracteres en str2 pero no en str1: {out2}")

# Ejemplo de uso
cadenas("alto", "altoc")
