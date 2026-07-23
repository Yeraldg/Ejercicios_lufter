print("---- ejercicio 1 ----")

counter1 = 1
ten_nums = []
counter2 = 0

while counter1 <= 10:
    try:
        current_num = int(input("por favor ingrese un numero al azar(total 10): "))
        ten_nums.append(current_num)
        counter1 += 1
    except ValueError:
        print("por favor ingrese un numero valido")
        
while True:
    try:
        choose_num = int(input("escoge un numero y te dire cuantas veces aparece en la lista: "))
        for num in ten_nums:
            if num == choose_num:
                counter2 += 1
        break
    except ValueError:
        print(" ingrese un numero valido")
print (f" la lista de numeros ingresados son: {ten_nums}")
print(f"el {choose_num} aparece {counter2} vez/veces en la lista")

print("----ejercicio 2 ----")

has_negative_zero = False

my_list = [1 , 1 , 2 , 3 , -4 ]
for i in my_list:
    if i <= 0:
        has_negative_zero = True

if has_negative_zero == True:
    print("hay al menos un numero negativo o cero")
else:
    print("todos son positivos")
    
print("----ejercicio 3 ----")

find_the_lowest = [ 7, 2 , 3 , 4 , 5 , 6]
lowest = find_the_lowest[0]
for num in find_the_lowest:
    if num < lowest:
        lowest = num

print (f"el menor valor es : {lowest}")

print("----ejercicio 4 ----")

got_list = []
list_counter = 1
sum_values = 0
greater_list = []
while True:
    try:
        element_num = int(input("para crear una lista, cuantos valores quiere ingresar? "))
        break
    except ValueError:
        print("ingrese un numero valido")

while list_counter <= element_num :
    try:
        num_provided = int(input("ingrese un numero para la lista: "))
        sum_values += num_provided
        got_list.append(num_provided)
        list_counter += 1
    except ValueError:
        print("ingrese un numero valido")
        
if element_num <= 0:
    print("no se puede calcular un promedio")
else:
    average = sum_values / element_num
    print(f" promedio: {average}")
    for num in got_list:
        if num > average:
            greater_list.append(num)
        

print(f"la nueva lista con los numeros mayores es: {greater_list}")

print("---- ejercicio 5 ----")

five_words = 0
initial_list = []
five_letter_list = []

while five_words < 5:
        current_word = input("por favor ingrese una palabra(total 5): ")
        if current_word.isalpha():
            initial_list.append(current_word)
            if len(current_word) > 4:
                five_letter_list.append(current_word)
            five_words += 1
        else:
            print("esa no es una palabra valida")
            
print(initial_list)
print (five_letter_list)