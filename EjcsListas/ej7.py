#Contar vocales consonantes
def contar_vocales_consonantes(texto):
    consonantes = set()
    vocales = set()
    for letra in texto:
        if letra not in ["a", "e", "i", "o", "u", " "]:
            consonantes.add(letra)
        else:
            vocales.add(letra)
    return f"{len(consonantes)} consonantes y {len(vocales)} vocales"

# Ejemplo de uso:
texto_ejemplo = "Hola mundo"
resultado = contar_vocales_consonantes(texto_ejemplo)
print(f"Texto original: {texto_ejemplo}")
print(f"Cantidad de consonantes y vocales: {resultado}")
