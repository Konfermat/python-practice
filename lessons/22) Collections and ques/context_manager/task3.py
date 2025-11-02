# Задача: реализовать менеджер контекста
# для работы с кэшом. Менеджер должен
# хранить кэш в словаре и автоматически
# очищать его при выходе из блока with.

class CacheManager:
    def __init__(self, cache_dict):
        self.cache = cache_dict
        print('кэш-менеджер инициализирован')

    def __enter__(self):
        print(f'текущий размер кэша {len(self.cache)}')
        return self.cache

                        # эти подписи нужены но не обязательны
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'текущий размер кэша {len(self.cache)}')
        self.cache.clear()
        print(f'новый размер: {len(self.cache)}')
        return False #если есть исключение будет переброшено

app_cache = {
    'user_1': 'data_a',
    'user_2': 'data_b',
    'session_id': '12345',
}

print('кэш до')
with CacheManager(app_cache) as cur_cache:
    print(f'кэш внутри блока {cur_cache}')
    cur_cache['new_key'] = 'new_value'
    print(f'кэш после добавления: {cur_cache}')
print(app_cache)