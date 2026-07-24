#jercicio 1

def read_lines():
    with open("ejercicios_extra/palabras_por_linea.txt" , "r") as file:
        lines = file.readlines()
    return lines

def to_strip(read_lines):
    word_list = []
    for word in read_lines:
        word_list.append(word.strip())
    return word_list

def to_sentence(word_list):
    sentence = " ".join(word_list)
    return sentence

def write_sentence(sentence):
    with open("ejercicios_extra/one_sentence.txt" , "w" , encoding="utf-8") as new_file:
        new_file.write(sentence)
        
write_sentence(to_sentence(to_strip(read_lines())))

#ejercicio 2

def read_file():
    with open("ejercicios_extra/palabras_por_linea.txt" , "r") as file:
        lines = file.readlines()
    return lines

def clean_lines(read_lines):
    lines_to_count = []
    for line in read_lines:
        lines_to_count.append(line.strip())
    return lines_to_count

def split_lines(lines_to_count):
    words_in_line = []
    for words in lines_to_count:
        words_in_line.extend(words.split())
    return words_in_line

def count_words(words_in_line):
    words_number = len(words_in_line)
    return words_number
    

print(f"Este archivo contiene {count_words(split_lines(clean_lines(read_file())))} palabras")

#ejercicio 3
    
def read_lowercase():
    with open("ejercicios_extra/palabras_por_linea.txt" , "r") as file:
        lines = file.readlines()
    return lines

def capitalize_text(lines):
    new_text = []
    for line in lines:
        upper = line.upper()
        new_text.append(upper)
    return new_text

def write_upper_file(new_text):
    with open("ejercicios_extra/upper_file.txt" , "w" , encoding="utf-8") as new_file:
        for line in new_text:
            new_file.write(line)

write_upper_file(capitalize_text(read_lowercase()))

#ejercicio 4

def add_to_file():
    new_line = input("escribe una linea de texto: ")
    
    with open("ejercicios_extra/file_to_extend.txt" , "a" , encoding="utf-8") as new_file:
            new_file.write(new_line + "\n")
            
    print("esta linea de texto fue agregada")
    
add_to_file()


