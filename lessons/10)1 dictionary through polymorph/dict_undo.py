class SmartHistoryDict:
    def __init__(self, initial_data=None):
        self.current_data = dict(initial_data or {})
        self.history = []
        self.save_state('Начальное состояние')

    def save_state(self, description):
        """Сохранение текущего состояния в историю"""
        self.history.append({
            'description': description,
            'data': self.current_data.copy(),
            'timestamp': len(self.history) #номер шага в истории
        })

    def __getitem__(self, key):
        if key not in self.current_data:
            raise KeyError(f'Ключ {key} не найден. '
                           f'Доступные ключи: '
                           f'{list(self.current_data.keys())}')
        return self.current_data[key]

    def __setitem__(self, key, value):
        old_data = self.current_data.get(key, 'не существовал')
        self.current_data[key] = value
        self.save_state(f'Установлен {key} = {value} (было {old_data})')


    def __delitem__(self, key):
        if key not in self.current_data:
            raise KeyError(f'Ключ {key} не найден'
                           f'Доступные ключи: '
                           f'{list(self.current_data.keys())}')
        old_value = self.current_data[key]
        del self.current_data[key]
        self.save_state(f'Удален {key} = {old_value}')

    def __len__(self):
        return len(self.current_data)

    def __iter__(self):
        return iter(self.current_data)

    def __contains__(self, key):
        return key in self.current_data

    def __str__(self):
        return f'SmartHistoryDict({self.current_data})'

    def get_history(self):
        return self.history.copy()

    def undo(self, step=1):
        """откатывает на указанное количество шагов назад"""
        if step >= len(self.history) or step < 1:
            raise ValueError('нельзя откатиться дальше начального состояния')
        target_index = len(self.current_data)-step-1
        self.current_data = self.history[target_index]['data'].copy()

        self.history = self.history[:target_index+1]
        self.save_state(f'Откат на {step} шагов')

    def get_state_at(self, timestamp):
        """возвращает состояние на определенном шаге"""
        if timestamp < 0 or timestamp >= len(self.history):
            raise ValueError('неверный номер шага')
        return self.history[timestamp]['data'].copy()

    def search_in_history(self, key):
        """ищет все изменеия определенного ключа в истории"""
        changes = []
        for state in self.history:
            if key in state['data']:
                changes.append({
                    'timestamp': state['timestamp'],#номер шага
                    'value': state['data'][key],#значение на этом шаге
                    'description': state['description']
                })
        return changes

def test_smart_dict():
    shd = SmartHistoryDict({'name': 'Sasha', 'age': 99})
    print(f'Начальное состояние: {shd}')

    shd['age'] = 10
    shd['city'] = 'NSK'
    shd['name'] = 'Vanya'
    print(f'\nПосле изменений: {shd}')

    del shd['city']
    print(f'\nПосле удаления city: {shd}')

    print('\n------ИСТОРИЯ-----')
    for state in shd.get_history():
        print(f'Шаг: {state["timestamp"]}: {state['description']}')

    print('\n-----ОТКАТ НА 2 ШАГА----')
    shd.undo(2)
    print(f'\nПосле отката: {shd}')

    print('\n-----ИЗМЕНЕНИЕ КЛЮЧА name---')
    name_history = shd.search_in_history('name')
    for change in name_history:
        print(f'Шаг: {change["timestamp"]}:'
              f'{change['value']} '
              f'({change['description']})')

if __name__ == '__main__':
    test_smart_dict()











