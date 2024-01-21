#Contar caracteres únicos
def contar_caracteres_unicos(texto):
    caracteres_unicos = set()
    for caracter in texto:
        # Paso 3: Almacenamiento en el conjunto
        caracteres_unicos.add(caracter)
    return len(caracteres_unicos)
# Ejemplo de uso:
texto_ejemplo = "Hola mundo"
resultado = contar_caracteres_unicos(texto_ejemplo)
print(f"Texto original: {texto_ejemplo}")
print(f"Número de caracteres únicos: {resultado}")
