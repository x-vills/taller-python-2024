#Crea un ciclo que me muestre los números pares desde 0 hasta un valor que se ingrese por teclado
input_number = int(input("Ingresa un número: "))

for start_index in range(input_number):
    if start_index % 2 == 0:
        print(start_index)