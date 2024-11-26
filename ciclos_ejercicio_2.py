#Crea un ciclo para que te genere los números del 1 a un valor ingresado por teclado
input_number = int(input("Ingresa un número: "))

for start_index in range(input_number):
    print(start_index+1)