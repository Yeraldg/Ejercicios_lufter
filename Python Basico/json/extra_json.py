import json

# ejercicio 1

def load_json_file(file_path):
    with open(file_path, "r" , encoding='utf-8') as file:
        data = file.read()
        reader = json.loads(data)
        return reader
    
def show_pokemon_info(reader):
    for pokemon in reader:
        print("-----------")
        print(f"Nombre: {pokemon['name']}")
        print(f"Tipo: {pokemon['type']}")
        print(f"Nivel: {pokemon['level']}")
        print(f"Velocidad general: {pokemon['stats']['speed']}")
        
        
#ejercicio 2

def organize_by_type(reader):
    pokemon_types = {}
    for pokemon in reader:
        pokemon_type = pokemon["type"]
        pokemon_type = pokemon_type.upper()
        if pokemon_type not in pokemon_types:
            pokemon_types[pokemon_type] = []
        pokemon_name = pokemon["name"]
        pokemon_types[pokemon_type].append(pokemon_name)
        
    return pokemon_types

def match_key(pokemon_types):
    while True:
        wanted_type = input("para buscar en nuestra base de datos, por favor escriba un tipo (en ingles) : ")
        wanted_type = wanted_type.strip().upper()
        if wanted_type in pokemon_types:
            
            return pokemon_types[wanted_type]
        else:
            right_language = input("escribio el tipo en ingles?: ")
            right_language = right_language.strip().upper()
            if right_language not in ("SI", "NO"):
                print(" por favor escriba solo : si o no")
                continue
            if right_language == "NO":
                print("intente de nuevo, en ingles")
                continue
            else:
                return None
            
def show_by_type(pokemon_list):
    if pokemon_list:
        print("Los pokemon que existen de ese tipo son:")
        for pokemon in pokemon_list:
            print(pokemon)
    else:
        print("No se encontraron pokemon de ese tipo")
        
#ejercicio 3

def show_pokemon_stats(reader):
    for pokemon in reader:
        print("-----------")
        print(f"Nombre: {pokemon['name']}")
        print(f"HP : {pokemon['stats']['hp']}")
        print(f"ataque : {pokemon['stats']['attack']}")
        print(f"defensa : {pokemon['stats']['defense']}")
        
#ejercicio 4
    
def organize_by_level(reader):
    pokemon_types = {}
    for pokemon in reader:
        pokemon_type = pokemon["type"]
        pokemon_type = pokemon_type.upper()
        if pokemon_type not in pokemon_types:
            pokemon_types[pokemon_type] = []
        pokemon_level = pokemon["level"]
        pokemon_types[pokemon_type].append(pokemon_level)
        
    return pokemon_types
    


def calculate_level_average(pokemon_types):
    print("-------------")
    for type_attribute in pokemon_types:
        levels = pokemon_types[type_attribute]
        level_sum = 0
        for level in levels:
            level_sum += level
        level_quantity = len(levels)
        average_level = level_sum / level_quantity
        print(f"Tipo: {type_attribute}: Promedio de nivel: {average_level}")


def main():
    file_path = "pokemon.json"
    data_list = load_json_file(file_path)
    show_pokemon_info(data_list)
    type_dict = organize_by_type(data_list)
    pokemon_list = match_key(type_dict)
    show_by_type(pokemon_list)
    show_pokemon_stats(data_list)
    pokemon_attribute_dict = organize_by_level(data_list)
    calculate_level_average(pokemon_attribute_dict)
    
main()