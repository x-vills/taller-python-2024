#Crea una condición que evalue más de dos posibilidades

person_age = int(input("Ingresa tu edad: "))
person_gender = int(input("Ingresa tu género (0. masculino, 1. femenino): "))

if person_age >= 18:
    if person_gender == 0:
        print("Bienvenido al servicio militar")
    elif person_gender == 1:
        print("El servicio militar es opcional, ¿Deseas continuar?")
    else:
        print("El género introducido no es válido")
else:
    print("Espera unos años más, aun no eres apt@ para el servicio militar")