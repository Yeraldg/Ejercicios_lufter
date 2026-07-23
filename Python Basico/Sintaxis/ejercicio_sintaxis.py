import random #al inicio del archiv0 como se me indico, parte del ejercicio 3
print("hola " + "lyfter")
#print("hola" + 7) *da error no se puede string + int
#print(7 + "hola") * da error no se puede int + string
list1 = ["casa" , "carro" , True]
list2 = ["mama" , "papa", False]
print(list1 +list2)
print("fiesta" , list1)
print(2.5 + 5)
print(True + False) #da 1 xq para el sistema es como binarios(1 + 0)

print("---- etapa de la vida ----")
name = input("cual es tu nombre: ")
lastname = input("cual es tu apellido?: ")
age = int(input("que edad tienes?: "))
if age <= 2:
    age_range = "sos un bebe"
elif age <= 10:
    age_range = "sos un niño"
elif age <= 13:
    age_range = "eres un preadolecente"
elif age < 18:
    age_range = "eres adolecente"
elif age <= 35:
    age_range = "eres joven adulto"
elif age < 65:
    age_range = "eres adulto"
else:
    age_range = "eres adulto mayor"
    
print(f"hola, {name} {lastname}, con {age} {age_range}")

print("---- adivina el numero ----")


secret = random.randint(1, 10)
number1 = 0
while number1 != secret:
    number1 = int(input("adivina el numero secreto del 1 al 10: "))
    if number1 != secret:
        print("incorrecto, intente de nuevo")
print("coreccto, el numero secreto era:" , secret)

print("---- mostrar mayor ----")

counter = 1
while counter <= 3:
    random_number = int(input("por favor ingrese un numero: "))
    if counter == 1:
        higher = random_number
    if higher < random_number:
        higher = random_number
    counter = counter + 1
print(f"el numero mayor de esos 3 es: {higher}")

print("---- los promedios ----")

pass_grades = 0
failed_grades = 0
counter = 1
pass_sum = 0
failed_sum  = 0
overall_sum = 0

all_grades = int(input("cuantas materias desea ingresar: "))
while counter <= all_grades:
    current_grade = int(input(f"por favor ingrese la nota numero {counter}: "))
    if current_grade < 70:
        failed_grades = failed_grades + 1
        failed_sum = failed_sum + current_grade
    else:
        pass_grades = pass_grades + 1
        pass_sum = pass_sum + current_grade
    
    
    overall_sum += current_grade
    counter += 1

overall_percentage = overall_sum / all_grades
if failed_grades > 0:
    percentage_failed = failed_sum / failed_grades
else:
    percentage_failed = 0
if pass_grades > 0:
    percentage_pass = pass_sum / pass_grades
else:
    percentage_pass = 0

print(f'el estudiante tiene esta cantidad de notas aprobadas: {pass_grades}')
print(f"este es el promedio de notas aprobadas: {percentage_pass}")
print(f"el estudiante tiene esta cantidad de notas desaprobadas: {failed_grades}")
print(f"este es el promedio de notas desaprobadas: {percentage_failed}")
print(f"este es el promedio total de notas: {overall_percentage}")

