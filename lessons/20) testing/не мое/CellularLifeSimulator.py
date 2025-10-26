from abc import ABC, abstractmethod
import uuid

# Ресурсы
class Nutrient:
    def __init__(self, x: int, y: int, amount: int):
        self.id: str = str(uuid.uuid4())
        self.x = x
        self.y = y
        self.amount = amount

    def is_empty(self) -> bool:
        return self.amount <= 0

    def consume(self, consumption_amount: int) -> int:
        consumed = min(consumption_amount, self.amount)
        self.amount -= consumed
        return consumed

    def __str__(self) -> str:
        return f'Nutrient (Pos = {self.x}, {self.y}), Type = {self.id}, Amount = {self.amount})'


class Cell(ABC):
    def __init__(self, x: int, y: int, level_energy: int=100):
        self.id: str = str(uuid.uuid4())
        self.x: int = x
        self.y: int = y
        self.level_energy = level_energy
        self.energy_cost = 5

    def is_alive(self) -> bool:
        return self.level_energy > 0

    def move(self, dx: int, dy: int) -> None:
        if not self.is_alive():
            return
        self.x += dx
        self.y += dy
        self.level_energy -= self.energy_cost
        if self.level_energy < 0:
            self.level_energy = 0

    @abstractmethod
    def interact(self, ecosystem: 'Ecosystem') -> None:
        pass

    def __str__(self)-> str:
        return f'{self.__class__.__name__}, (ID:{self.id[:4]}, Pos = ({self.x}, {self.y}), Energy = {self.level_energy})'

class HerbivoreCell(Cell):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.metabolism_rate: int = 25 # сколько веществ потребляет

    def interact(self, ecosystem: 'Ecosystem') -> None:
        if not self.is_alive():
            return
        nutrient = ecosystem.get_nutrient_at(self.x, self.y)
        if nutrient:
            consumed = nutrient.consume(self.metabolism_rate)
            self.level_energy += consumed


class CarnivoreCell(Cell):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, level_energy=200)
        self.attack_power = 50 # сколько энергии отнимает у жертвы

    def interact(self, ecosystem: 'Ecosystem') -> None:
        if not self.is_alive():
            return

        target_cell = ecosystem.get_target_herbivore_at(self.x, self.y, self.id)

        if target_cell:
            stolen_energy = min(self.attack_power, target_cell.level_energy)

            target_cell.level_energy -= stolen_energy
            self.level_energy -= stolen_energy

# украденная энергия куда и движение

class Ecosystem:
    def __init__(self):
        # по ID
        self.cells = {}
        # по type
        self.nutrients = {}

    def add_cell(self, cell: Cell) -> None:
        self.cells[cell.id] = cell

    def add_nutrient(self, nutrient: Nutrient) -> None:
        self.nutrients[nutrient.id] = nutrient

    def get_nutrient_at(self, x: int, y: int):
        for nutrient in self.nutrients.values():
            if nutrient.x == x and nutrient.y == y and not nutrient.is_empty():
                return nutrient
        return None

    def get_target_herbivore_at(self, x: int, y: int, attacker_id: str):
        for cell in self.cells.values():
            if cell.x == x and cell.y == y and cell.is_alive() and isinstance(cell, HerbivoreCell) and cell.id != attacker_id:
                return cell
        return None

    def cleanup(self) -> None:
        dead_cells_ids = [id for id, cell in self.cells.items() if not cell.is_alive()]
        for id in dead_cells_ids:
            del self.cells[id]

        depleted_nutrient_ids = [id for id, nutrient in self.nutrients.items() if nutrient.is_empty()]
        for id in depleted_nutrient_ids:
            del self.nutrients[id]

    def run_cycle(self):
        # Движение клеток
        for cell in self.cells.values():
            cell.move(1, 0)

        # взаимодействие
        for cell in self.cells.values():
            cell.interact(self)

        self.cleanup()

        return len(self.cells), len(self.nutrients)

    def __str__(self):
        return f'Ecosystem:(Cells={len(self.cells)}, Nutrients={len(self.nutrients)})'

def setup_simulator():
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

    print('Циклы симуляции')

    for c in range(1, 5):
        num_cells, num_nutr = eco.run_cycle()
        print(f'{c}: cells={num_cells}, nutrients={num_nutr}, energy h_a{herb_a.level_energy}, carn_a{carn_a.level_energy}')

    print('Финальное состояние')
    print(eco)

if __name__ == '__main__':
    setup_simulator()