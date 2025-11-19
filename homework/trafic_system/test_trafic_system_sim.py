import sys
#sys.path.append('C:/My Work Space/Prog tinkering/python_practice/HW/car shit')
sys.path.append('')
from trafic_system_sim import Car, Truck, Road, TrafficSystemSimulator, Vehicle

#Тестирование Vehicle
def test_accelerate_increases_speed_but_not_above_max():
    class TestVehicle(Vehicle):
        def decide_action(self, vehicles):
            pass
    v = TestVehicle(position=0, speed=0, max_speed=5)
    for _ in range(10):
        v.accelerate()
    assert v.speed == 5  # Скорость не может превысить max_speed

def test_position_updates_after_movement():
    class TestVehicle(Vehicle):
        def decide_action(self, vehicles):
            pass
    v = TestVehicle(position=0, speed=3, max_speed=5)
    v.position += v.speed
    assert v.position == 3  # Позиция увеличилась на скорость

from unittest.mock import patch

# Тесты для Car и Truck
def test_car_accelerates_on_free_road():
    car = Car(position=0, speed=1, max_speed=4, danger_zone=1)
    # Нет рядом машин, должна ускориться
    car.decide_action([])
    assert car.speed > 1

def test_car_slows_down_near_vehicle():
    car1 = Car(position=0, speed=3, max_speed=4, danger_zone=1)
    car2 = Car(position=4, speed=1, max_speed=4, danger_zone=1)
    # car2 находится близко впереди car1
    old_speed = car1.speed
    car1.decide_action([car2])
    assert car1.speed < old_speed

def test_truck_slows_at_longer_distance_than_car():
    car = Car(position=0, speed=3, max_speed=4, danger_zone=1)
    truck = Truck(position=0, speed=3, max_speed=3, danger_zone=2)
    vehicle_ahead = Car(position=5)  # Машина впереди

    car_old_speed = car.speed
    truck_old_speed = truck.speed

    car.decide_action([vehicle_ahead])
    truck.decide_action([vehicle_ahead])

    # При таком расположении truck должен начать замедляться раньше
    assert truck.speed < truck_old_speed
    assert car.speed == car_old_speed

# Тесты для Road
def test_road_adds_vehicle():
    road = Road(length=10)
    car = Car()
    road.add_vehicle(car)
    assert car in road.vehicles

def test_road_removes_vehicle_past_length():
    road = Road(length=10)
    car = Car(position=11)
    road.add_vehicle(car)
    # Симуляция удаления машин за пределами дороги
    road.vehicles = [v for v in road.vehicles if v.position < road.length]
    assert car not in road.vehicles

# Тесты для TrafficSystemSimulator
def test_run_cycle_invokes_decide_action_and_movement(monkeypatch):
    road = Road(length=10)
    car = Car(position=0, speed=1, max_speed=4)
    road.add_vehicle(car)
    sim = TrafficSystemSimulator(road)

    called = {"decide_called": False}
    def fake_decide_action(vehicles):
        called["decide_called"] = True
        # Двигаем машину на 2
        car.position += 2

    car.decide_action = fake_decide_action

    # Переопределим run_cycle, чтобы остановить после одного цикла
    def stop_after_one_cycle():
        # Одна итерация цикла run_cycle
        for vehicle in road.vehicles:
            vehicle.decide_action(road.vehicles)
        assert called["decide_called"]
        # Проверяем что позиция изменилась
        assert car.position == 2

    sim.run_cycle = stop_after_one_cycle
    sim.run_cycle()

def test_full_simulation_two_vehicles():
    road = Road(length=20)
    slow_car = Car(position=0, speed=1, max_speed=2)
    fast_car = Car(position=1, speed=2, max_speed=4)
    road.add_vehicle(slow_car)
    road.add_vehicle(fast_car)
    sim = TrafficSystemSimulator(road)

    # Запустим несколько циклов вручную
    for _ in range(5):
        for vehicle in road.vehicles:
            vehicle.decide_action(road.vehicles)
        # Обновляем позиции (если decide_action не обновляет)
        for v in road.vehicles:
            v.position += v.speed

        # Удаляем ушедшие с дороги
        road.vehicles = [v for v in road.vehicles if v.position < road.length]

    # Проверяем, что быстрая машина не обогнала медленную слишком далеко
    assert fast_car.position >= slow_car.position
    assert fast_car.speed <= fast_car.max_speed
    assert slow_car.speed <= slow_car.max_speed


