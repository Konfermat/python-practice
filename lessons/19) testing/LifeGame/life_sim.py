from abc import ABC, abstractmethod
import uuid


class Nutrient:
    def __init__(self, x: int, y: int, type: str, amount: int):
        self.x = x
        self.y = y
        self.type = type
        self.amount = amount
        self.is_alive = True

    def is_empty(self) -> bool:
        return self.amount <= 0

    def __str__(self) -> str:
        return f'Nutrient: Pos=({self.x}, {self.y}, Type={self.type}, Amount={self.amount})'


class Cell(ABC):
    def __init__(self, x: int, y: int, initial_energy: int = 100):
        self.id: str = str(uuid.uuid4())
        self.x: int = x
        self.y: int = y
        self.energy = initial_energy
        self.energy_cost = 5

    def is_alive(self):
        return self.energy > 0

    def move(self, dx: int, dy: int) -> None:
        if not self.is_alive:
            return
        self.x += dx
        self.y += dy
        self.energy -= self.energy_cost
        if self.energy < 0:
            self.energy = 0

    @abstractmethod
    def interact(self, ecosystem: 'Ecosystem'):
        pass

    def __str__(self):
        return f'{self.__class__.__name__} (ID:{self.id}, Pos=({self.x}, {self.y}), Energy={self.energy})'


class HerbivoreCell(Cell):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.metabolism_rate: int = 25  # сколько веществ потребляет экземпляр

    def interact(self, ecosystem: 'Ecosystem')->None:
        if not self.is_alive():
            return
        nutrient = ecosystem.get_nutrient_at(self.x, self.y)
        if nutrient:
            nutrient.amount -= self.metabolism_rate
            self.energy += self.metabolism_rate


class CarnivoreCell(Cell):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, initial_energy=200)
        self.attack_power = 50

    def interact(self, ecosystem: 'Ecosystem')->None:
        if not self.is_alive():
            return
        target_cell = ecosystem.get_target_herb_at(self.x, self.y)
        if target_cell:
            target_cell.energy = self.attack_power
            self.energy += target_cell.metabolism_rate

# украденная энергия куда и движение

    def interact(self, ecosystem: 'Ecosystem'):
        pass

    class Ecosystem:
        def __init__(self):
            self.cells = {}
            self.nutrients = {}

        def add_cell(self, cell: Cell) -> None:
            self.cells[cell.id] = cell

        def add_nutrients(self, nutrient: Nutrient) -> None:
            self.nutrients[nutrient.type] = nutrient

        def get_nutrient(self, x: int, y: int):
            for nutrient in self.nutrients.values():
                if nutrient.x == x and nutrient.y == y and not nutrient.is_empty():
                    return nutrient
            return None

        def get_target_herb_at(self, x: int, y: int, attacker_id: str):
            for cell in self.cells.values():
                if cell.x == x and cell.y == y and cell.is_alive() and cell.id != attacker_id:
                    return cell
            return None

        def cleanup(self) -> None:
            dead_cells_ids = [id for id, cell in self.cells.items() if not cell.is_alive]

            for id in dead_cells_ids:
                del self.cells[id]

            empty_nutrient_types = [type for type, nutrient in self.nutrients.items() if nutrient.is_empty()]

            for type in empty_nutrient_types:
                del self.nutrients[type]

            def run_cycle(s):
                for cell in self.cells.values():
                    cell.move(1, 0)

                for cell in self.cells.values():
                    cell.interact(self)

                self.cleanup()
                return len(self.cells), len(self.nutrients)

# id generator
# print(uuid.uuid4())
