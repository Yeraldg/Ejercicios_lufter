print("---- ejercicio 1 ----")

def get_name():
    while True:
        try:
            name = input("por favor ingrese su nombre: ")
            if name.isdigit():
                raise ValueError("no se permiten numeros")
            elif not name.replace(" " , "").isalpha():
                raise ValueError("solo se permiten letras y espacios entre palabras")
        
            break
        except ValueError as error:
            print(error)
    return name
            
def get_age():
    while True:
        try:
            age = int(input("por favor ingrese su edad, no escrito: "))
            break
        except ValueError:
            print("por favor utilice formato de numero")
    return age
            
def main():
    name = get_name()
    age = get_age()
            
    print(f"Hola! {name} su edad es {age} años.")
    
main()

print("---- ejercicio 2 ----")

got_list =  ['4', 'hola', '10', '5.2']

def convert_to_int(got_list):
        for item in got_list:
            try:
                number = int(item)
                print(f"{item} convertido a int : {number}")
            except ValueError:
                print("no se pudo convertir a int: " + (item))
            
convert_to_int(got_list)

print("---- ejercicio 3 ----")

new_list = ['10', 'manzana', '5.5', '3', 'n/a']

def sum_values(new_list):
    total = 0
    for posible_float in new_list:
        try:
            usable_number = float(posible_float)
            total += usable_number
            print(f"{posible_float} sumado correctamente")
        except ValueError:
            print("elemento invalido: " + (posible_float))
            
    print(f"total de la suma: {total}")
            
sum_values(new_list)