#Crea una condición que te permita verificar si un valor ingresado es par o impar

input_number = int(input("Ingresa un número: "))

if input_number % 2 == 0:
     if input_number % 3 == 0:
          print(f"El número {input_number} es par y es multiplo 3")
     else:
        print(f"El número {input_number} es par")
else:
     if input_number % 3 == 0:
          print(f"El número {input_number} es impar y es multiplo 3")
     else:
        print(f"El número {input_number} es impar")