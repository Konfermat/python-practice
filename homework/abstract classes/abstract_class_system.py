from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.completed_tasks = 0
    
    @abstractmethod
    def work(self, task):
        pass
    
    def __lt__(self, other):
        if self.completed_tasks < other.completed_tasks:
            return True
        else:
            return False
            
    def __gt__(self, other):
        if self.completed_tasks > other.completed_tasks:
            return True
        else:
            return False
    
    def __eq__(self, other):
        if self.completed_tasks == other.completed_tasks:
            return True
        else:
            return False
    
    def __str__(self):
        return f'Имя: {self.name}\nРоль: {self.role}'
    

class Developer(Employee):
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.completed_tasks = 0
    def work(self):
        return f'{self.name} программирует.'

class Tester(Employee):
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.completed_tasks = 0
    def work(self):
        return f'{self.name} тестирует.'

class Manager(Employee):
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.completed_tasks = 0
    def work(self):
        return f'{self.name} делает вид что работает.'

class LeadDeveloper(Developer, Manager):
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.completed_tasks = 0
    def work(self):
        return f'{self.name} программирует и руководит.'

class Task:
    def __init__(self, task_name, employee):
        self.task_name = task_name
        self.employee = employee
        
    def finish_task(self):
        self.employee.completed_tasks += 1
        print(f'{self.employee.work()} завершена работа над: "{self.task_name}".')
    
class Project:
    def __init__(self, name):
        self.name = name

    d1 = Developer('Гоша', 'Фронтэнд')
    t1 = Tester('Олег', 'Мануальщик')
    m1 = Manager('Дмитрий', 'Руководитель отдела')
    ld1 = LeadDeveloper('Вася', 'Руководитель-архитектор')
    
    task1 = Task('Починить старую машину', d1)
    task2 = Task('Построить пасеку', t1)
    task3 = Task('Поковырятся в носу', ld1)
    task4 = Task('Протестируй сделаное ЛИДом', t1)
    
    task1.finish_task()
    task2.finish_task()
    task3.finish_task()
    task4.finish_task()
    print()
    
    print(f'Работник {d1.name}, {d1.role}. Задач сделано: {d1.completed_tasks}.')
    print(f'Работник {t1.name}, {t1.role}. Задач сделано: {t1.completed_tasks}.')
    print(f'Работник {m1.name}, {m1.role}. Задач сделано: {m1.completed_tasks}.')
    print(f'Работник {ld1.name}, {ld1.role}. Задач сделано: {ld1.completed_tasks}.')
    print()
    
    print(d1 < t1)
    print(d1 > t1)
    print(d1 == t1)

    def __str__(self):
        return f''

print(Project('Проект_НСНГ'))

