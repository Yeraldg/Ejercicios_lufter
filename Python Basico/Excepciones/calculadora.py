def get_number(message):

    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("por favor utilice formato de numero")

def show_menu():

    while True:

        print("Escoja dentro de estas opciones:")
        print("para Sumar digite : 1")
        print("para Restar digite : 2")
        print("para Multiplicar digite : 3")
        print("para Dividir digite : 4")
        print("para borrar el numero escogido digite : 5")
        print("para salir digite : 6")

        try:
            operator = int(input("por favor ingrese el numero de la operacion que desea usar, no escrito: "))

            if operator < 1 or operator > 6:
                print("digite un numero del 1 al 6")
                continue

            return operator

        except ValueError:
            print("por favor utilice formato de numero")

def get_second_number(operator):

    while True:

        number_to_operate = get_number("por favor ingrese el segundo numero de la operacion, no escrito: ")

        if operator == 4 and number_to_operate == 0:
            print("no se puede dividir entre cero")
            continue

        return number_to_operate


def calculate(current_number, operator, number_to_operate):

    if operator == 1:
        current_number = current_number + number_to_operate

    elif operator == 2:
        current_number = current_number - number_to_operate

    elif operator == 3:
        current_number = current_number * number_to_operate

    elif operator == 4:
        current_number = current_number / number_to_operate

    return current_number


def main():

    print("ejercicio : Calculadora")

    current_number = get_number("por favor ingrese el primer numero de la operacion, no escrito: ")

    while True:

        operator = show_menu()

        if operator == 6:
            print("fin.")
            break

        if operator == 5:
            current_number = 0
            print(f"Valor reiniciado: {current_number}")
            continue

        number_to_operate = get_second_number(operator)

        current_number = calculate(current_number, operator, number_to_operate)

        print(f"el valor obtenido es : {current_number}")

main()

        

