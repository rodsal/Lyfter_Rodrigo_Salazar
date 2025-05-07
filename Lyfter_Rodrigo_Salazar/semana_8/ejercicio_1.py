def read_file(path):
    songs_list = []
    with open(path) as file:
        for line in file.readlines():
            songs_list.append(line)
    return songs_list

def write_file(path,list):
    with open(path, "w", encoding='utf-8') as file:
        for song in list:
            file.write(song)

path = "/Users/nicoleportuguez/Library/Mobile Documents/com~apple~CloudDocs/Lyfter/Modulo 1/Semana 8/Ejercicio manejo de archivos/Lista_de_canciones.txt"
song_list = read_file(path)
song_list.sort()
write_file(path,song_list)