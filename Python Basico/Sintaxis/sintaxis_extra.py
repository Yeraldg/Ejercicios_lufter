print("---- mostrar precio ----")

product_price = int(input("por favor ingrese el precio del producto: "))
if product_price < 100:
    discount = product_price * 0.02
else:
    discount = product_price * 0.1
final_price = product_price - discount

print(f"el precio ya aplicado el descuento es de: {final_price}")

print("calcular el tiempo")
while True:
    try:
        seconds = int(input("por favor ingrese un tiempo en segundos:"))
        break
    except ValueError:
        print(" error, ingrese un numero valido")
if seconds < 600:
    missing_seconds = 600 - seconds
    print(f" {missing_seconds} segundos faltantes para 10 min")
elif seconds > 600:
    print("esto es mayor a 10 minutos")
else:
    print("es igual a 10 min")
    
print("----suma del 1 al numero ingresado ----")

counter = 1
num_sum = 0
while True:
    try:
        limit_num = int(input("por favor ingrese un numero: "))
        break
    except ValueError:
        print("por favor ingrese un numero valido")
while counter <= limit_num:
    num_sum += counter
    counter += 1
print(f"el resultado es: {num_sum}")

print("---- el numero secreto ----")

secret = 7

while True:
    try:
        guess_number = int(input("ingresa un numero del 1 al 10 y te dire si acertaste: "))
        if guess_number not in range(1 , 11):
            print("numero fuera de rango")
            continue
        if guess_number == secret:
            print("acertaste")
            break
        else:
            print("incorrecto")
    except ValueError:
        print("intente un numero valido")
        
print("---- el famoso 30 ----")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if (num1 == 30 or num2 == 30 or num3 == 30 or
    num1 + num2 + num3 == 30):
    print("Correcto")
else:
    print("Incorrecto")
        
print("---- la temperatura ----")


while True:
    try:
        celsius = int(input("ingrese la temperatura en celcius: "))
        break
    except ValueError:
        print("ingrese un numero valido ")
        continue
        
farenheit = (celsius * 9/5) + 32
kelvin = celsius  + 273.15

print(f"ahora te convertire {celsius} a: ")
print(f"Farenheit = {farenheit}")
print(f"kelvin = {kelvin}")

print(" ---- tabla de multiplicar ----")

while True:
    try:
        multi_num = int(input("ingrese un numero del 1 al 10: "))
        if multi_num not in range(1 , 11):
            print("ingrese un numero del 1 al 10")
            continue
        break
    except ValueError:
        print("ingrese un numero valido")

for i in range( 1 , 13):
    print(f"{multi_num} x {i} = {multi_num * i}")