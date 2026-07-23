print("----ejercicio 1 ----")

def print_hi_presentation():
    print("hola, mi nombre es Mau")
    print_study_academy()
    
def print_study_academy():
    print("y estudio en lyfter")

print_hi_presentation()

print("----ejercicio 2 ----")

variable = 10

def use_local_variable():
    variable = 15
    return variable

multiplier = 2

local_variable = use_local_variable()

external_sum = variable * multiplier

internal_sum = local_variable * multiplier

print(external_sum)
print(internal_sum)
print(variable)
print(use_local_variable())

print("---- ejercicio 3 ----")

numbers = [4, 6, 2, 29]


def sum_numbers(numbers):
    total_result = 0
    
    for num in numbers:
        total_result += num 
    return total_result

    
print(sum_numbers(numbers))

print("---- ejercicio 4 ----")

text = "hola"

def go_backwards(text):
    new_text = ""
    
    for letter in range(len(text) -1 ,-1 , -1):
        new_text += text[letter]
        
    return new_text
    
print(go_backwards(text))

print("---- ejercicio 5 ----")

paragraph = "I love Nación Sushi"

def analyze_case(paragraph):
    upper_count = 0
    
    lower_count = 0
    
    for case in paragraph:
        if case.isupper():
            upper_count += 1
        elif case.islower():
            lower_count += 1

    print(f"there's {upper_count} upper cases and {lower_count} lower cases")
    
analyze_case(paragraph)

print("---- ejercicio 6 ----")

hypen_words = input("pot favor ingrese palabras separadas por guiones (-): ")

def order_words(hypen_words):
    unsorted_list = hypen_words.split("-")
    unsorted_list.sort()
    ordered_list = "-".join(unsorted_list)
    
    print(ordered_list)

order_words(hypen_words)

print("---- ejercicio 7 ----")

all_numbers = [1, 4, 6, 7, 13, 9, 67]

def is_prime(number):
    if number <= 1:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True

def get_primes(all_numbers):
    prime_numbers = []
    
    for number in all_numbers:
        if is_prime(number):
            prime_numbers.append(number)
            
    return prime_numbers
    
print(get_primes(all_numbers))
