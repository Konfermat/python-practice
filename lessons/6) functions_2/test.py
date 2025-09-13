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

