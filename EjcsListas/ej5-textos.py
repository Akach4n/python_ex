import string

def contar_palabras_unicas(texto):
    # Eliminar signos de puntuación y convertir a minúsculas
    translator = str.maketrans("", "", string.punctuation)
    texto = texto.translate(translator).lower()
    print(texto)

    # Dividir el texto en palabras y contar las únicas
    palabras = texto.split()
    palabras_unicas = set(texto)

    return len(palabras_unicas)

# Ejemplo de uso:
texto_ejemplo = "Hola mundo, mundo maravilloso. Hola, Hola, mundo!"
resultado = contar_palabras_unicas(texto_ejemplo)
print(f"Texto original: {texto_ejemplo}")
print(f"Número de palabras únicas: {resultado}")

