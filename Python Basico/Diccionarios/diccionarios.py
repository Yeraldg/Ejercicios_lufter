print("---- ejercicio 1 ----")

hotel = {"nombre" : "Guxuly",
        "numero de estrellas" : 5,
        "habitaciones" : [ {"numero" : 101,
                            "piso" : 1,
                            "precio por noche" : 50} ,
                            {"numero" : 102,
                            "piso" : 1 ,
                            "precio por noche" : 50},
                            {"numero" : 201,
                            "piso" : 2,
                            "precio por noche" : 90},
                            {"numero" : 303,
                            "piso" : 3,
                            "precio por noche" : 110}]}

print("ejercicio 2")

game_keys = ["nombre de juego" , "heroe" , "habilidad" , "meta"]

values = ["mario bros" ,"luigi" , "asustarse" , "ganar"]

game_data  = {}

for i in range(len(game_keys)):
    game_data[game_keys[i]] = values[i]

print(game_data)

print("ejercicio 3")

personal_info = {"nombre" : "Yerald",
                "apellido" : "Garcia",
                "edad" : 39,
                "Email" : "Yeralg_6@hotmail.com",
                "pasatiempo" : "gamer"}

keys_to_hide = ["edad" , "pasatiempo"]

for key in keys_to_hide:
    personal_info.pop(key)
    
print(personal_info)