def read_songs():
    with open("canciones.txt" , "r") as file:
        songs = file.readlines()
    return songs

def sort_songs(songs):
    clean_songs = []
    for song in songs:
        clean_songs.append(song.strip())
    clean_songs.sort()
    return clean_songs

def write_songs(ordered_songs):
    with open("ordered_songs.txt" , "w" , encoding="utf-8") as new_file:
        for song in ordered_songs:
            new_file.write(song + "\n")
            
def main():
    songs = read_songs()
    print(songs)
    ordered_songs = sort_songs(songs)
    print(ordered_songs)
    write_songs(ordered_songs)
    
main()