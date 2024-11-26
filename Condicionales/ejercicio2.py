#Crea una condición que te permita verificar si un valor es mayor o menor que 20

input_number = int(input("Ingresa un número: "))

if input_number > 20:
    if input_number % 3 == 0:
        print(f"El número {input_number} es mayor a 20 y es multiplo de 3")
    else:
        print(f"El número {input_number} es mayor a 20")
else:
    if input_number % 3 == 0:
        print(f"El número {input_number} no es mayor a 20 y es multiplo de 3")
    else:
        print(f"El número {input_number} no es mayor a 20")