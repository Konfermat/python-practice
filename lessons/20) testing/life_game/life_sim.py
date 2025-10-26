from abc import ABC, abstractmethod
import uuid

# Ресурсы
class Nutrient:
    def __init__(self, x: int, y: int, amount: int):
        self.id: str = str(uuid.uuid4())  # добавлен
        self.x: int = x
        self.y: int = y
        self.amount: int = amount

    def is_empty(self) -> bool:
        return self.amount <= 0

    def consume(self, consumption_amount: int) -> int:
        #потребляет указанное количество ресурса
        consumed = min(consumption_amount, self.amount)
        self.amount -= consumed
        return consumed  #фактическое потребленное количество

    def __str__(self) -> str:
        return (f'Nutrient(ID={self.id[:4]}, '
                f'Pos=({self.x}, {self.y}), '
                f'Amount={self.amount})')


class Cell(ABC):
    def __init__(self, x: int, y: int, initial_energy: int = 100):
        self.id: str = str(uuid.uuid4())
        self.x: int = x
        self.y: int = y
        self.energy: int = initial_energy
        self.energy_cost: int = 5  #расход энергии за ход

    def is_alive(self) -> bool:
        return self.energy > 0

    def move(self, dx: int, dy: int) -> None:
        if not self.is_alive():
            return
        self.x += dx
        self.y += dy
        self.energy -= self.energy_cost
        if self.energy < 0:
            self.energy = 0

    @abstractmethod
    def interact(self, ecosystem: 'Ecosystem') -> None:
        pass

    def __str__(self) -> str:
        return (f'{self.__class__.__name__}'
                f'(ID:{self.id[:4]}, Pos=({self.x}, {self.y}), '
                f'Energy={self.energy})')


class HerbivoreCell(Cell):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, initial_energy=150)
        self.metabolism_rate: int = 25  #сколько веществ потребляет за раз

    def interact(self, ecosystem: 'Ecosystem') -> None:
        if not self.is_alive():
            return
        nutrient = ecosystem.get_nutrient_at(self.x, self.y)
        if nutrient:
            consumed = nutrient.consume(self.metabolism_rate)
            self.energy += consumed  #энергия увеличивается на потребленное количество
        #если ресурса нет, просто нет взаимодействия, энергия не меняется


class CarnivoreCell(Cell):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, initial_energy=200)
        self.attack_power: int = 50  #сколько энергии отнимает у жертвы

    def interact(self, ecosystem: 'Ecosystem') -> None:
        if not self.is_alive():
            return
        # передаем свой ID, чтобы не атаковать самого себя
        target_cell = ecosystem.get_target_herbivore_at(self.x, self.y, self.id)

        if target_cell:
            # расчет украденной энергии не больше, чем есть у жертвы, и не больше attack_power
            stolen_energy = min(self.attack_power, target_cell.energy)

            target_cell.energy -= stolen_energy  #жертва теряет энергию
            self.energy += stolen_energy  # хищник получает украденную энергию

# украденная энергия куда и движение
class Ecosystem:
    def __init__(self):
        # по ID
        self.cells = {}
        #храним Nutrient по ID, чтобы иметь несколько ресурсов
        self.nutrients = {}

    def add_cell(self, cell: Cell) -> None:
        self.cells[cell.id] = cell

    def add_nutrient(self, nutrient: Nutrient) -> None:
        #добавляем по ID
        self.nutrients[nutrient.id] = nutrient

    def get_nutrient_at(self, x: int, y: int):
        for nutrient in self.nutrients.values():
            if nutrient.x == x and nutrient.y == y and not nutrient.is_empty():
                return nutrient
        return None

    def get_target_herbivore_at(self, x: int, y: int, attacker_id: str):
        for cell in self.cells.values():
            if (cell.x == x and cell.y == y and
                    cell.is_alive() and
                    isinstance(cell, HerbivoreCell) and
                    cell.id != attacker_id):
                #проверка типа HerbivoreCell
                return cell
        return None

    def cleanup(self) -> None:
        dead_cell_ids = [id for id, cell in self.cells.items()
                         if not cell.is_alive()]
        for id in dead_cell_ids:
            del self.cells[id]

        #удаление по ID, а не по type
        depleted_nutrient_ids = [id for id, nutrient in self.nutrients.items()
                                 if nutrient.is_empty()]
        for id in depleted_nutrient_ids:
            del self.nutrients[id]

    def run_cycle(self) -> tuple[int, int]:
       # 1Движение
        for cell in self.cells.values():
            cell.move(1, 0)

#         2 взаимодействие
        for cell in self.cells.values():
            cell.interact(self)

        self.cleanup()

        return len(self.cells), len(self.nutrients)
    
    def __str__(self):
        return f'Cells = {len(self.cells)}, Nutrients = {len(self.nutrients)}'
    
def setup_simulation():
    eco = Ecosystem()

    # добавляем ресурсы
    eco.add_nutrient(Nutrient(2, 0, 50))
    eco.add_nutrient(Nutrient(3, 0, 50))
    eco.add_nutrient(Nutrient(10, 0, 100))

    # добавляем клетки
    herb_a = HerbivoreCell(0, 0)
    herb_b = HerbivoreCell(5, 0)
    carn_a = CarnivoreCell(1, 0)

    eco.add_cell(herb_a)
    eco.add_cell(herb_b)
    eco.add_cell(carn_a)

    print(eco)
    print(herb_a)
    print(carn_a)

    print('цикл симуляции')
    for c in range(1, 5):
        num_cells, num_nutr = eco.run_cycle()
        print(f'{c}: cells={num_cells}, nutrients={num_nutr}, energy h_a={herb_a.energy}, carn_a={carn_a.energy}')
    
    print('финальное состояние')
    print(eco)

setup_simulation()