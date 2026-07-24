print("---- ejercicio 1 ----")

def analyze_word(got_text , got_letter):
    letter_count = 0
    for letter in got_text:
        if letter == got_letter:
            letter_count += 1
            
    return(f"la letra esta {letter_count} vez/veces en la palabra inicial")

while True:
    try:
        got_text = input("por favor ingrese una palabra o texto: ")
        if not got_text.replace(" " , "").isalpha():
            raise ValueError("solo se permiten letras y espacios entre palabras")
        break
    except ValueError as error:
        print(error)

while True:
    try:
        got_letter = input("por favor ingrese una letra: ")

        if len(got_letter) != 1 or not got_letter.isalpha():
            raise ValueError("solo se permite 1 letra")
        break
    except ValueError as error:
        print(error)
            
print(analyze_word(got_text , got_letter))

print("---- ejercicio 2 ----")

words_list = ["casa" , "avion" , "calabaza", "luna" , "cuarto"]

letters_to_exceed = 4


def filtered_words(words_list , letters_to_exceed):
    longer_words = []
    for word in words_list:
        if len(word) > letters_to_exceed:
            longer_words.append(word)
    return(longer_words)
    
print(filtered_words(words_list , letters_to_exceed))

print("---- ejercicio 3 ----")

while True:
    try:
        words_gotten= input("por favor ingrese una palabra o texto: ")
        if not words_gotten.replace(" " , "").isalpha():
            raise ValueError("solo se permiten letras y espacios entre palabras")
        break
    except ValueError as error:
        print(error)
        
def got_vocals(words_gotten):
    vocals = ["a" , "e" , "i" , "o" , "u"]
    vocal_count = 0
    words_gotten.replace(" " , "")
    for character in words_gotten:
        if character.lower() in vocals:
            vocal_count += 1
    return vocal_count

print(got_vocals(words_gotten))