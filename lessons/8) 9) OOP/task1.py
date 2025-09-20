# args и kwargs практика

class Employee:
    def __init__(self, name, position, salary, **kwargs):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return f'Имя: {self.name} Должность: {self.position}, Зарплата: {self.salary}'

class Manager(Employee):
    def __init__(self, team_size, **kwargs):
        super().__init__(**kwargs)
        self.team_size = team_size

    def get_info(self):
        return super().get_info() + f' Размер команды: {self.team_size}'

class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language

    def write_code(self):
        return f'Пишет код на языке {self.programming_language}'

class TechLead(Manager, Developer):
    # яндекс чампионат по программ

    # так нельзя
    # Manager.__init__(self, name, position, salary, team_size)
    # Developer.__init__(self, name, position, salary, team_size, programming_language)
    def __init__(self, name, position, salary, team_size, programming_language):
        super().__init__(name=name, position=position, salary=salary, team_size=team_size, programming_language=programming_language)

t1 = TechLead('Ivan', "TechLead", 30000, 10, "Python")
t1.write_code()
print(t1.get_info())