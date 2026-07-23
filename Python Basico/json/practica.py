import json

# ejercicio 1

def load_json_file(file_path):
    with open(file_path, "r" , encoding='utf-8') as file:
        data = file.read()
        reader = json.loads(data)
        return reader
    
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
        
    return (pokemon_types)
    


def calculate_level_average(pokemon_types):
    for type_attribute in pokemon_types:
        levels = pokemon_types[type_attribute]
        level_sum = 0
        for level in levels:
            level_sum += level
        level_quantity = len(levels)
        average_level = level_sum / level_quantity
        print(f"Tipo: {type_attribute}: Promedio de nivel: {average_level}")
        





file_path = "pokemon.json"
data_list = load_json_file(file_path)
pokemon_attibute_dict = organize_by_level(data_list)
calculate_level_average(pokemon_attibute_dict)


