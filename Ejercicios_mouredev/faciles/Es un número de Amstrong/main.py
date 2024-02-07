def numero_armstrong(numero : str):
    nume = []
    for n in numero:
        elevado = pow(int(n), len(numero))
        nume.append(elevado)
    suma = sum(nume)
    if suma == int(numero):
        print(f"El número {numero} es un número Amstrong")
    else:
        print(f"El número {numero} no es un número Amstrong")


numero = input("Dame un número: ")

numero_armstrong(numero)
