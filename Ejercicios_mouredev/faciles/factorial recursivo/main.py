# def factorial_recursivo(n):
#     # Caso base: el factorial de 0 es 1
#     if n == 0:
#         return 1
#     # Caso recursivo: n! = n * (n-1)!
#     else:
#         return n * factorial_recursivo(n-1)

n = 5
f = n
for cur in range(n,1,-1):
    f = f * (cur - 1)
print(f)


# Ejemplo de uso
# numero = 5
# resultado = factorial_recursivo(numero)
# print(f"El factorial de {numero} es: {resultado}")
