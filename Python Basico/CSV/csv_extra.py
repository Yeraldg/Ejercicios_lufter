#ejercicio 1

import csv

def read_videogame_csv(file_path):
    with open(file_path, "r" , encoding='utf-8') as file:
        reader = csv.reader(file)
        first_row = next(reader)
        for line in reader:
            print(f"{first_row[0]} : {line[0]}")
            print(f"{first_row[1]} : {line[1]}")
            print(f"{first_row[2]} : {line[2]}")
            print(f"{first_row[3]} : {line[3]}")
            print("------------")
            

#ejercicio 2

def get_classification():
    classification = input("por favor ingrese la clasifficacion ESRB, para verificar en nuestra base de datos: ")
    esrb = classification.strip().upper()
    return esrb

def load_file_games(file_path):
    with open(file_path, "r" , encoding='utf-8') as file:
        reader = csv.DictReader(file)
        loaded_games = list(reader)
        return loaded_games
            
def find_matching_esrb(esrb, loaded_games):
    lines =[]
    for line in loaded_games:
        if esrb == line["classification_esrb"]:
            lines.append(line)
    return lines

#ejercicio 3

def genre_count(loaded_games):
    genres_count = {}
    for game in loaded_games:
        if game["genre"] not in genres_count:
            genres_count[game["genre"]] = 1
            
        else:
            genres_count[game["genre"]] = genres_count[game["genre"]] + 1
    return genres_count

def show_genre_count(genres_count):
    print("Cantidad de juegos por género:")
    for genre in genres_count:
        print(f"{genre}: {genres_count[genre]}")

#ejercicio 4

def get_dev():
    dev = input("por favor ingrese la desarrollador, para verificar en nuestra base de datos: ")
    developer = dev.strip().upper()
    return developer

def find_matching_dev(developer, loaded_games):
    games =[]
    for game in loaded_games:
        upper_dev = game["dev"].strip().upper()
        if developer == upper_dev:
            games.append(game)
    return games

def show_games_by_dev (games):
    print(f"videjuegos desarrollados por: {games[0]['dev']}")
    for game in games:
        print(f" - {game['title']} (Clasificación: {game['classification_esrb']}, Género: {game['genre']})")

def main():
    file_path = "videogame_comma.csv"
    read_videogame_csv(file_path)
    got_classification = get_classification()
    finder = load_file_games(file_path)
    match_games = find_matching_esrb(got_classification, finder)
    for game in match_games:
        print(game)
    if not match_games:
        print("no se encontraron juegos con esa clasificacion")
    genre_counter = genre_count(finder)
    show_genre_count(genre_counter)
    dev_group = get_dev()
    developer_list = find_matching_dev(dev_group, finder)
    if not developer_list:
        print("ese desarrollador no se encontro en la base de datos")
    else:
        show_games_by_dev(developer_list)

main()           