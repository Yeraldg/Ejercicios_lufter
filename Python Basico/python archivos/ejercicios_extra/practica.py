#ejercicio 4

def add_to_file():
    new_line = input("escribe una linea de texto: ")
    
    with open("ejercicios_extra/file_to_extend.txt" , "a" , encoding="utf-8") as new_file:
            new_file.write(new_line + "\n")
            
    print("esta linea de texto fue agregada")
    
add_to_file()
