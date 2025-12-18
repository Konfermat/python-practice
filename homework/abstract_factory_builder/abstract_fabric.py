from abc import ABC, abstractmethod

# Абстрактные классы
class HouseFactory(ABC):
    @abstractmethod
    def create_door(self) -> object:
        pass
    @abstractmethod
    def create_window(self) -> object:
        pass
    @abstractmethod
    def create_wall(self) -> object:
        pass                
    @abstractmethod
    def create_roof(self) -> object:
        pass
    @abstractmethod
    def create_garage(self) -> object:
        pass
        
class Door(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass
        
class Window(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass
        
class Wall(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass           
        
class Roof(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass           

class Garage(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass           

class HouseBuilder(ABC):
    @abstractmethod
    def build_doors(self, count: int) -> None:
        pass        
    @abstractmethod
    def build_windows(self, count: int) -> None:
        pass
    @abstractmethod
    def build_walls(self) -> None:
        pass
    @abstractmethod
    def build_roof(self) -> None:
        pass
    @abstractmethod
    def build_garage(self) -> None:
        pass

# Конкретный класс House
class House:
    def __init__(self):
        self.elements = []
        self.door_data = [0, 0]
        self.window_data = [0, 0]
        self.wall_data = [0, 0]
        self.roof_data = [0, 0]
        self.garage_data = [0, 0]
    
    def scan_elements(self):
        """Сканирует элементы и обновляет счетчики"""
        self.door_data = [0, 0]
        self.window_data = [0, 0]
        self.wall_data = [0, 0]
        self.roof_data = [0, 0]
        self.garage_data = [0, 0]
        
        for i, elem in enumerate(self.elements):
            elem_type = str(type(elem))[8:-2]  # Убираем '<class ' и '>'
            if 'Door' in elem_type:
                self.door_data[0] = i
                self.door_data[1] += 1
            elif 'Window' in elem_type:
                self.window_data[0] = i
                self.window_data[1] += 1
            elif 'Wall' in elem_type:
                self.wall_data[0] = i
                self.wall_data[1] += 1
            elif 'Roof' in elem_type:
                self.roof_data[0] = i
                self.roof_data[1] += 1
            elif 'Garage' in elem_type:
                self.garage_data[0] = i
                self.garage_data[1] += 1        
    
    def display(self):
        self.scan_elements()
        print('Этот дом обладает следующими отличительными особенностями:')  
        
        if self.door_data[1] == 0:
            print('Двери не построены.')
        else:
            print(f'{self.elements[self.door_data[0]].describe()} (установлено {self.door_data[1]} шт.)')
            
        if self.window_data[1] == 0:
            print('Окна не построены.')
        else:
            print(f'{self.elements[self.window_data[0]].describe()} (установлено {self.window_data[1]} шт.)')                
            
        if self.wall_data[1] == 0:
            print('Стены не построены.')
        else:
            print(f'{self.elements[self.wall_data[0]].describe()}')
            
        if self.roof_data[1] == 0:
            print('Крыша не построена.')
        else:
            print(f'{self.elements[self.roof_data[0]].describe()}')                

        if self.garage_data[1] == 0:
            print('Гараж: Нет')
        else:
            print(f'{self.elements[self.garage_data[0]].describe()}')                        

# Фабрики
class ModernHouseFactory(HouseFactory):
    def create_door(self):
        class ModernDoor(Door):
            def describe(self):
                return 'Двери: Стеклянная раздвижная дверь' 
        return ModernDoor()    

    def create_window(self):
        class ModernWindow(Window):
            def describe(self):
                return 'Окна: Панорамное безрамное окно'        
        return ModernWindow()
        
    def create_wall(self):
        class ModernWall(Wall):
            def describe(self):
                return 'Стены: Стеклянные панели'
        return ModernWall()     
        
    def create_roof(self):
        class ModernRoof(Roof):
            def describe(self):
                return 'Крыша: Плоская эксплуатируемая крыша' 
        return ModernRoof()
        
    def create_garage(self):
        class ModernGarage(Garage):
            def describe(self):
                return 'Гараж: Да' 
        return ModernGarage() 

class ClassicHouseFactory(HouseFactory):
    def create_door(self):
        class ClassicDoor(Door):
            def describe(self):
                return 'Двери: Дубовая филенчатая дверь'        
        return ClassicDoor()    

    def create_window(self):
        class ClassicWindow(Window):
            def describe(self):
                return 'Окна: Деревянное окно со ставнями'        
        return ClassicWindow()
        
    def create_wall(self):
        class ClassicWall(Wall):
            def describe(self):
                return 'Стены: Кирпичная кладка'
        return ClassicWall()     
        
    def create_roof(self):
        class ClassicRoof(Roof):
            def describe(self):
                return 'Крыша: Двускатная черепичная крыша' 
        return ClassicRoof()  
    
    def create_garage(self):
        class ClassicGarage(Garage):
            def describe(self):
                return 'Гараж: Да' 
        return ClassicGarage()  

class VictorianHouseFactory(HouseFactory):
    def create_door(self):
        class VictorianDoor(Door):
            def describe(self):
                return 'Двери: Массивная дубовая дверь'        
        return VictorianDoor()    

    def create_window(self):
        class VictorianWindow(Window):
            def describe(self):
                return 'Окна: Арочные окна с витражами'        
        return VictorianWindow()
        
    def create_wall(self):
        class VictorianWall(Wall):
            def describe(self):
                return 'Стены: Каменные стены с резьбой'
        return VictorianWall()     
        
    def create_roof(self):
        class VictorianRoof(Roof):
            def describe(self):
                return 'Крыша: Сложная многоскатная крыша' 
        return VictorianRoof()  
    
    def create_garage(self):
        class VictorianGarage(Garage):
            def describe(self):
                return 'Гараж: Да' 
        return VictorianGarage()  

# Строитель
class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self, house_factory: object):
        self.house_factory = house_factory
        self.house = House()

    def build_doors(self, count: int) -> None:
        for _ in range(count):
            self.house.elements.append(self.house_factory.create_door())

    def build_windows(self, count: int) -> None:
        for _ in range(count):
            self.house.elements.append(self.house_factory.create_window())
        
    def build_walls(self) -> None:
        self.house.elements.append(self.house_factory.create_wall())
        
    def build_roof(self) -> None:
        self.house.elements.append(self.house_factory.create_roof())
        
    def build_garage(self) -> None:
        self.house.elements.append(self.house_factory.create_garage())
        
    def get_result(self) -> object:
        return self.house  # Просто возвращаем готовый дом

# Директор
class Director:
    def __init__(self):
        self.modern_house_factory = ModernHouseFactory()
        
    def build_modern_house(self, builder) -> None:
        builder.house_factory = self.modern_house_factory
        builder.build_walls()
        builder.build_windows(3)
        builder.build_doors(1)
        builder.build_roof()
        builder.build_garage()

# Функции сборки
def standart_build():
    modern_factory = ModernHouseFactory()
    builder = ConcreteHouseBuilder(modern_factory)
    director = Director()
    director.build_modern_house(builder)
    modern_house = builder.get_result()
    print("=== СТАНДАРТНЫЙ СОВРЕМЕННЫЙ ДОМ ===")
    modern_house.display()

def custom_build1():
    classic_factory = ClassicHouseFactory()
    custom_builder = ConcreteHouseBuilder(classic_factory)
    custom_builder.build_walls()
    custom_builder.build_doors(3)
    custom_builder.build_windows(5)
    custom_builder.build_roof()
    # Гараж НЕ строим
    custom_house = custom_builder.get_result()
    print("\n=== КАСТОМНЫЙ КЛАССИЧЕСКИЙ ДОМ ===")
    custom_house.display()

def custom_build2():
    victorian_factory = VictorianHouseFactory()
    custom_builder = ConcreteHouseBuilder(victorian_factory)
    custom_builder.build_walls()
    custom_builder.build_doors(3)
    custom_builder.build_windows(5)
    custom_builder.build_roof()
    # Гараж НЕ строим
    custom_house = custom_builder.get_result()
    print("\n=== КАСТОМНЫЙ ВИКТОРИАНСКИЙ ДОМ ===")
    custom_house.display()

# Запуск
if __name__ == "__main__":
    standart_build()
    custom_build1()
    custom_build2()
