# ejercicio 1
#solucion 1, usando la reciente inf0 (insert)

base_words1 = ["la" , "es" , "marino"]

extra_words2 = ["casa" , "azul" , "claro"]

base_words1.insert(1 , extra_words2[0])
base_words1.insert(3 , extra_words2[1])
base_words1.insert(5 , extra_words2[2])
print(base_words1)
print(" ".join(base_words1))

#solucion 2, por que ya vimos *for/in

base_words3 = ["la" , "es" , "marino"]

extra_words4 = ["casa" , "azul" , "claro"]

position = 1

for palabra in extra_words4:
    base_words3.insert(position , palabra)
    position += 2
    
print(base_words3)
print(" ".join(base_words3))

#SOLUCION 3, segun entiendo de lo pedido

base_words5 = ["la", "es", "marino"]
extra_words6 = ["casa", "azul", "claro"]

for i in range(len(base_words5)):
    print(base_words5[i], extra_words6[i])

print("---- ejercicio 2 ----")

frase = "Mi nombre es Yerald"

for i in range(len(frase) -1 , -1 , -1):
    print(frase[i])
    
#ejercicio 3

da_list = [6 , 2 , 3 , 4 , 5, 1]

last = da_list[0]
da_list[0] = da_list[-1]
da_list[-1] = last
print(da_list)

print('---- ejercicio 4 ----')

all_nums  = [1, 2 , 3 , 4 , 5 ,6 , 7 , 8 , 9]

for elements in range(len(all_nums) -1 , -1 , -1):
    if all_nums[elements] % 2:
        all_nums.pop(elements)
        
print(all_nums)

print('---- ejercicio 5 ----')

ten_nums = []
counter = 1

while counter<= 10:
    try:
        current_number = int(input("por favor ingrese un numero(total 10 numeros):"))
        ten_nums.append(current_number)
        if counter == 1:
            higher = current_number
        if current_number > higher:
            higher = current_number
        counter += 1
    except ValueError:
        print("digite un numero valido")

print (ten_nums)
print(f'el mas alto fue {higher}')
