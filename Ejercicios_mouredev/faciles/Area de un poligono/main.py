def calcular_area(poligono: str):
    if poligono == "Triángulo":
        medida = str(input("Dime la medida a usar: "))
        base = float(input("Dime su base: "))
        altura = float(input("Dime su altura: "))
        resultado = float((base * altura) / 2)
        print(f"El área del triángulo es: {resultado} {medida}²")
    elif poligono == "Cuadrado":
        medida = str(input("Dime la medida a usar: "))
        lado = float(input("Dime su lado: "))
        resultado = float(lado * lado)
        print(f"El área del cuadrado es: {resultado} {medida}²")
    elif poligono == "Rectángulo":
        medida = str(input("Dime la medida a usar: "))
        base = float(input("Dime su base: "))
        altura = float(input("Dime su altura: "))
        resultado = float(base * altura)
        print(f"El área del rectángulo es: {resultado} {medida}²")


poligono = str(input("Bienvenido a la calculadora de áreas, elija entre Triángulo, Cuadrado o Rectángulo\n"))
calcular_area(poligono)