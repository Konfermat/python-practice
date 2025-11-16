from abc import ABC, abstractmethod

class Road:
    def __init__(self, length, lanes):
        self.length = length
        self.lanes = lanes
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_off_road_vehicles(self):
        self.vehicles = [v for v in self.vehicles if v.position < self.length]

class Vehicle(ABC):
    def __init__(self, vehicle_id, position, speed, max_speed):
        self.vehicle_id = vehicle_id
        self.position = position
        self.speed = speed
        self.max_speed = max_speed

    def accelerate(self, acceleration):
        self.speed = min(self.speed + acceleration, self.max_speed)

    def move(self):
        self.position += self.speed

    @abstractmethod
    def decide_action(self, road):
        pass

class Car(Vehicle):
    SAFE_DISTANCE = 10
    ACCELERATION = 2
    DECELERATION = -3

    def decide_action(self, road):
        for vehicle in road.vehicles:
            if vehicle is not self and vehicle.position > self.position and vehicle.position - self.position <= self.SAFE_DISTANCE:
                self.speed = max(self.speed + self.DECELERATION, 0)
                return
        self.accelerate(self.ACCELERATION)

class Truck(Vehicle):
    SAFE_DISTANCE = 20
    ACCELERATION = 1
    DECELERATION = -2

    def decide_action(self, road):
        for vehicle in road.vehicles:
            if vehicle is not self and vehicle.position > self.position and vehicle.position - self.position <= self.SAFE_DISTANCE:
                self.speed = max(self.speed + self.DECELERATION, 0)
                return
        self.accelerate(self.ACCELERATION)

class TrafficFlowSimulator:
    def __init__(self, road):
        self.road = road

    def add_vehicle(self, vehicle):
        self.road.add_vehicle(vehicle)

    def run_cycle(self):
        for vehicle in self.road.vehicles:
            vehicle.decide_action(self.road)
        for vehicle in self.road.vehicles:
            vehicle.move()
        self.road.remove_off_road_vehicles()

# --- Пример использования ---
road = Road(length=100, lanes=3)
simulator = TrafficFlowSimulator(road)
car1 = Car(vehicle_id=1, position=0, speed=5, max_speed=20)
truck1 = Truck(vehicle_id=2, position=15, speed=3, max_speed=10)
simulator.add_vehicle(car1)
simulator.add_vehicle(truck1)
simulator.run_cycle()

# --- Тесты ---
import unittest

class TestTrafficFlowSimulator(unittest.TestCase):
    def test_vehicle_accelerate_and_move(self):
        v = Car(vehicle_id=1, position=0, speed=5, max_speed=20)
        v.accelerate(3)
        self.assertEqual(v.speed, 8)
        v.move()
        self.assertEqual(v.position, 8)

    def test_car_decide_action_free_road(self):
        road = Road(length=100, lanes=2)
        car = Car(vehicle_id=1, position=0, speed=5, max_speed=20)
        road.add_vehicle(car)
        car.decide_action(road)
        self.assertEqual(car.speed, 7)

    def test_car_decide_action_with_obstacle(self):
        road = Road(length=100, lanes=2)
        car1 = Car(vehicle_id=1, position=0, speed=10, max_speed=20)
        car2 = Car(vehicle_id=2, position=5, speed=10, max_speed=20)
        road.add_vehicle(car1)
        road.add_vehicle(car2)
        car1.decide_action(road)
        self.assertLess(car1.speed, 10)

    def test_truck_decide_action_cautious(self):
        road = Road(length=100, lanes=2)
        truck = Truck(vehicle_id=1, position=0, speed=5, max_speed=10)
        car = Car(vehicle_id=2, position=15, speed=5, max_speed=20)
        road.add_vehicle(truck)
        road.add_vehicle(car)
        truck.decide_action(road)
        self.assertLess(truck.speed, 5)

    def test_road_add_and_remove_vehicle(self):
        road = Road(length=20, lanes=1)
        car = Car(vehicle_id=1, position=19, speed=5, max_speed=20)
        road.add_vehicle(car)
        self.assertIn(car, road.vehicles)
        car.move()
        road.remove_off_road_vehicles()
        self.assertNotIn(car, road.vehicles)

    def test_traffic_flow_simulator_sequence(self):
        road = Road(length=100, lanes=2)
        sim = TrafficFlowSimulator(road)
        car = Car(vehicle_id=1, position=0, speed=5, max_speed=20)
        sim.add_vehicle(car)
        sim.run_cycle()
        self.assertEqual(car.position, 7)



if __name__ == '__main__':
    unittest.main()
