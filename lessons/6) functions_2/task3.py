# Напишите функцию load_playlist(), которая загружает данные в
# список словарей:
# {"artist": "Imagine Dragons", "title": "Believer", "duration": "3:24"}
# Напишите функцию sort_by_duration(playlist), которая сортирует
# песни по продолжительности.
# Напиши функцию save_sorted_playlist(filename), которая сохраняет
# отсортированный плейлист в новый файл.
# Дополнительно: реализовать поиск песен по исполнителю.

def load_playlist():
    playlist = []
    try:
        with open('playlist.txt', 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(' - ')
                if len(parts) >= 3:
                    song = {
                        'artist': parts[0],
                        'name': parts[1],
                        'duration': parts[2]
                    }
                    playlist.append(song)
        return playlist
    except FileNotFoundError:
        return []


def duration_to_seconds(duration):
    try:  # map(function, itter_operation)
        minutes, seconds = map(int, duration.split(':'))
        # for el in duration:
        #     els = [int(x) for x in el.split(':')]
        #     minutes, seconds = els
        return minutes * 60 + seconds

    except ValueError:
        return 0

def sort_by_duration(playlist):
    return sorted(playlist, key=lambda x: duration_to_seconds(x['duration']))

def save_sorted_playlist(filename):
    playlist = load_playlist()
    sorted_playlist = sort_by_duration(playlist)

    with open(filename, 'w', encoding='utf-8' ) as file:
        for song in sorted_playlist:
            file.write(f'{song["artist"]} - {song["name"]} - {song["duration"]}\n')

def search_by_artist(artist_name):
    playlist = load_playlist()
    result = []

    for song in playlist:
        if artist_name.lower() in song['artist'].lower():
            return result.append(song)

    return result
def test():
    playlist = load_playlist()
    print(playlist)
    sort_playlist = sort_by_duration(playlist)
    print(sort_playlist)
    save_sorted_playlist('sorted_playlist.txt')
    art = input('Введите имя исполнителя: ')
    print(search_by_artist(art))

# любой файл будет называться __main__
if __name__ == '__main__':
    test()

# НЕ РАБОТАЕТ? ДА И ХУЙ С НИМ!