def convertir_decimal_a_binario(numero: int):
    restos = []
    while numero > 0:
        resto = numero % 2
        numero = numero // 2
        restos.append(str(resto))

    num_binario = "".join(restos[::-1])
    print(f"El número {decimal} en binario es: {num_binario}")

decimal = int(input("Dime un número decimal para convertir a binario:\n"))
convertir_decimal_a_binario(decimal)

