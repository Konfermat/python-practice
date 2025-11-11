

# MVC

# Model
# View
# Controller
# Архитектурный паттерн
# Каждый класс ответственный за свою задачу

class CounterModel:
    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._observers = [] # трекер изменений
    def get_value(self):
        return self._value
    def increment(self):
        self._value += 1
        self._notify()
    def decrement(self):
        self._value -= 1
        self._notify()
    def _notify(self):
        for observer in self._observers:
            observer.update()
    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

class CounterView:
    def __init__(self, model, controller):
        self.model = model
        self.controller = controller
    def display_counter(self):
        curr_value = self.model.get_value()
        print(f'текущее значение: {curr_value}')
    def update(self):
        print('получено уведомление об изменении данных')
        self.display_counter()
    def get_user_action(self):
        print('действия:')
        action = input('i, d, q\n').strip().lower()
        return self.controller.handle_action(action)

class  CounterController:
    def __init__(self, model):
        self.model = model
    def handle_action(self, action):
        if action == 'i':
            self.model.increment()
        elif action == 'd':
            self.model.decrement()
        elif action == 'q':
            return False
        else:
            print('проигнорировано')
        return True

def main():
    counter_model = CounterModel(initial_value=5)
    counter_controller = CounterController(counter_model)
    counter_view = CounterView(counter_model, counter_controller)
    counter_model.add_observer(counter_view)
    counter_view.display_counter()
    run = True
    while run:
        run = counter_view.get_user_action()

if __name__ == '__main__':
    main()
