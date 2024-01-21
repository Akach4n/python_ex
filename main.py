# Importamos las librerías random para generar la contraseña y string para los caracteres
import random
import string
#Mostramos el menú
print("Generador de contraseñas")
print("1. Generar contraseña")
print("2. Salir")
#Pedimos la opción
opcion = int(input("Seleccione una opción: "))

#Comprobamos la opción
if opcion == 1:
    #Pedimos la longitud de la contraseña
    longitud = int(input("Indique la longitud de la contraseña: "))
    #Generamos una variable con los caracteres que se van a utilizar
    caracteres = string.ascii_letters + string.digits + string.punctuation
    #Generamos una lista vacía para guardar la contraseña
    contraseña = []
#Generamos un bucle para generar la contraseña
    for i in range(longitud):
        #Generamos un caracter aleatorio
        caracter_random = random.choice(caracteres)
        #Añadimos el caracter a la lista por cada bucle
        contraseña.append(caracter_random)
        #Convertimos la lista en un string
    contraseña = "".join(contraseña)
    #Mostramos la contraseña
    print("Contraseña generada: " + contraseña)
#Si la opción es 2, salimos del programa
elif opcion == 2:
    print("Gracias por utilizar el generador de contraseñas")
    exit()
#Si la opción no es 1 o 2, mostramos un mensaje de error3
else:
    print("Opción no válida")


