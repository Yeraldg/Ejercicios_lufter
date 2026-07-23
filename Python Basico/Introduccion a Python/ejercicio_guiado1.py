print("----Clasificador de nivel de gamer ----")
name = input("ingresa tu nombre: ")
hours = int(input("cuantas horas llevas jugando?: "))
is_competitive = input("juegas competitivo? (si/no): ")
if hours < 10:
    category = "Noob"
    message = "bienvenido al mundo gaming"
elif hours < 50:
    category = "casual"
    message = "ya le estas agarrando el ritmo"
elif hours < 200:
    category = "gamer"
    message = "definitivamente sabes lo que haces"
elif hours >= 200 and is_competitive == "si":
    category = "pro"
    message = "eres una leyenda viviente"
else:
    category = "gamer"
    message = "tienes la experiencia pero aun no entras al competitivo"
    
print(f"{name}, tu categoria es: {category}")
print(message)
