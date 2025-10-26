import pytest
from task4_main import Nutrient, HerbivoreCell, CarnivoreCell, Ecosystem

#фикстуры
# будем создавать базовые объекты для каждого теста


@pytest.fixture
def basic_nutrient():
    return Nutrient(0, 0, 50)

@pytest.fixture
def basic_herbivore():
    return HerbivoreCell(10, 10)

@pytest.fixture
def basic_carnivore():
    return CarnivoreCell(5, 5)

@pytest.fixture
def basic_ecosystem():
    return Ecosystem()


# тесты для Nutrient
class TestNutrient:
    def test_initial_state(self, basic_nutrient):
        #начальное состояние ресурса
        assert basic_nutrient.x == 0
        assert basic_nutrient.y == 0
        assert basic_nutrient.amount == 50
        assert not basic_nutrient.is_empty()

    def test_consume_partial(self, basic_nutrient):
        #частичное состояние ресурса
        consumed = basic_nutrient.consume(20)
        assert consumed == 20
        assert basic_nutrient.amount == 30
        assert not basic_nutrient.is_empty()

    def test_consume_full(self, basic_nutrient):
        #потребление всего ресурса и его истощение
        consumed = basic_nutrient.consume(50)
        assert consumed == 50
        assert basic_nutrient.amount == 0
        assert basic_nutrient.is_empty()

    def test_consume_over(self, basic_nutrient):
        consumed = basic_nutrient.consume(100)
        assert consumed == 50
        assert basic_nutrient.amount == 0
        assert basic_nutrient.is_empty()

# тесты для Cell
class TestCellBaseLogic:
    def test_initial_energy(self, basic_herbivore):
        assert basic_herbivore.energy == 150
        assert basic_herbivore.is_alive()

    def test_consume_energy(self, basic_herbivore):
        # движение уменьшает энергию и меняет координаты
        initial_energy = basic_herbivore.energy
        initial_x = basic_herbivore.x
        cost = basic_herbivore.energy_cost
        basic_herbivore.move(dx=2, dy=1)
        assert basic_herbivore.x == initial_x + 2
        assert basic_herbivore.y == 10 - 1
        assert basic_herbivore.energy == initial_energy - cost

    def test_death_by_energy_zero(self, basic_herbivore):
        basic_herbivore.energy = 5
        basic_herbivore.move(1, 0)
        assert basic_herbivore.energy == 0
        assert not basic_herbivore.is_alive()

    def test_dead_cell_cannot_move(self, basic_herbivore):
        basic_herbivore.energy = 0
        basic_herbivore.x = 10
        basic_herbivore.move(1, 0)
        assert basic_herbivore.x == 10


class TestHerbivoreCell:
    def test_interact_eats(self, basic_herbivore, basic_ecosystem):
        #Проверяем что потребляем ресурс на той же позиции
        basic_herbivore.x = 5
        basic_herbivore.y = 5
        nutrient = Nutrient(5, 5, 100)
        basic_ecosystem.add_nutrient(nutrient)

        initial_energy = basic_herbivore.energy
        metabolism = basic_herbivore.metabolism_rate
        basic_herbivore.interact(basic_ecosystem)

        assert basic_herbivore.energy == initial_energy + metabolism
        assert nutrient.amount == 100 - metabolism

    def test_interact_no_nutrient(self, basic_herbivore, basic_ecosystem):
        # Энергия не меняется если нет ресурса
        initial_energy = basic_herbivore.energy
        # (10, 10) нет ресурсов
        basic_herbivore.interact(basic_ecosystem)
        assert basic_herbivore.energy == initial_energy

class TestCarnivoreCell:
    def test_interact_attacks_herbivore(self, basic_herbivore, basic_ecosystem, basic_carnivore):
        # Проверяем успешную атаку хищника
        basic_carnivore.x = 5
        basic_carnivore.y = 5
        basic_herbivore.x = 5
        basic_herbivore.y = 5

        basic_ecosystem.add_cell(basic_carnivore)
        basic_ecosystem.add_cell(basic_herbivore)

        c_initial_energy = basic_carnivore.energy
        h_initial_energy = basic_herbivore.energy

        attack_power = basic_carnivore.attack_power

        basic_carnivore.interact(basic_ecosystem)

        assert basic_carnivore.energy == c_initial_energy + attack_power
        assert basic_herbivore.energy == h_initial_energy - attack_power

    def test_interact_no_target(self, basic_carnivore, basic_ecosystem):
        basic_carnivore.x = 5
        basic_carnivore.y = 5
        c_initial_energy = basic_carnivore.energy

        basic_carnivore.interact(basic_ecosystem)
        assert basic_carnivore.energy == c_initial_energy


    def test_interact_kills_target(self, basic_carnivore, basic_herbivore, basic_ecosystem):
        basic_herbivore.energy = 30
        basic_carnivore.x = 5
        basic_carnivore.y = 5
        basic_herbivore.x = 5
        basic_herbivore.y = 5

        basic_ecosystem.add_cell(basic_herbivore)
        basic_ecosystem.add_cell(basic_carnivore)

        c_initial_energy = basic_carnivore.energy

        basic_carnivore.interact(basic_ecosystem)

        assert basic_herbivore.energy == 0
        assert basic_carnivore.energy == c_initial_energy + 30

class TestEcosystem:
    def test_cleanup_dead_cells(self, basic_ecosystem, basic_herbivore):
        herb_a = basic_herbivore
        herb_b = HerbivoreCell(1, 1)
        herb_b.energy = 0

        basic_ecosystem.add_cell(herb_a)
        basic_ecosystem.add_cell(herb_b)

        assert len(basic_ecosystem.cells) == 2

        basic_ecosystem.cleanup()

        assert len(basic_ecosystem.cells) == 1
        assert herb_a.id in basic_ecosystem.cells

    def test_cleanup_removes_nutrients(self, basic_ecosystem, basic_nutrient):
        nutrient_a = basic_nutrient
        nutrient_b = Nutrient(1, 1, 0)

        basic_ecosystem.add_nutrient(nutrient_a)
        basic_ecosystem.add_nutrient(nutrient_b)

        assert len(basic_ecosystem.nutrients) == 2
        basic_ecosystem.cleanup()
        assert len(basic_ecosystem.nutrients) == 1
        assert nutrient_a.id in basic_ecosystem.nutrients

    def test_run_cycle(self, basic_ecosystem):
        #движение, взаимодействие и очистка
        herb = HerbivoreCell(0, 0)
        carn = CarnivoreCell(1, 0)

        initial_h_energy = herb.energy #150
        initial_c_energy = carn.energy #200
        cost = herb.energy_cost #5
        attack = carn.attack_power #50

        basic_ecosystem.add_cell(herb)
        basic_ecosystem.add_cell(carn)

        # движение на (1, 0) нет атаки
        basic_ecosystem.run_cycle()
        basic_ecosystem.run_cycle()
        basic_ecosystem.run_cycle()
        basic_ecosystem.run_cycle()
        basic_ecosystem.run_cycle()

        eco = Ecosystem()
        herb_collision = HerbivoreCell(1, 0)
        carn_collision = CarnivoreCell(1, 0)
        eco.add_cell(herb_collision)
        eco.add_cell(carn_collision)
        h_energy = herb_collision.energy #150
        c_energy = carn_collision.energy #200

        #цикл столкновения
        num_cells, num_nutrients = eco.run_cycle()

        # движение(обе клетки перемещаются)

        assert herb_collision.x == 2
        assert carn_collision.x == 2

        # взаимодействие
        assert herb_collision.energy == h_energy - cost - attack
        assert carn_collision.energy == c_energy - cost + attack
        assert num_cells == 2






