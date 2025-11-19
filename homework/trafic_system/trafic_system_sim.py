import time
import os
from abc import ABC, abstractmethod
import uuid

class Road:
    def __init__(self, length=10, direction='right'):
        self.length = length
        self.direction = direction
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

class Vehicle(ABC):
    def __init__(self, position=0, speed=0, max_speed=0, danger_zone=0):
        self.position = position
        self.speed = speed
        self.max_speed = max_speed
        self.ID = uuid.uuid4()
        self.danger_zone = danger_zone

    def accelerate(self):
        if self.speed < self.max_speed:
            self.speed += 1

    def slow(self):
        if self.speed > 0:
            self.speed -= 1

    @abstractmethod
    def decide_action(self, vehicles):
        pass

class Car(Vehicle):
    def __init__(self, position=0, speed=1, max_speed=4, danger_zone=1):
        super().__init__(position, speed, max_speed, danger_zone)
        
    def decide_action(self, vehicles):
        cars_position = [i.position for i in vehicles if not i.ID == self.ID]
        slow_case = range(self.position, self.position + self.speed + self.danger_zone)
        regular_case = range(self.position, self.position + self.speed + self.danger_zone + 1)
        acceleration_case = range(self.position, self.position + self.speed + self.danger_zone + 2)
        dz_cars = range(self.position, self.position + self.danger_zone + 1)

        for i in cars_position:
            if i in dz_cars:
                # никуда не сдвинусь
                return
            elif i in slow_case:
                self.slow()
                return
            elif i in regular_case:
                self.slow()
                self.position += self.speed
                return
            elif i in acceleration_case:
                self.position += self.speed
                return

        # если нет машин поблизости, ускоряемся и едем
        self.accelerate()
        self.position += self.speed

class Truck(Vehicle):
    def __init__(self, position=0, speed=1, max_speed=3, danger_zone=2):
        super().__init__(position, speed, max_speed, danger_zone)
    def decide_action(self, vehicles):
        cars_position = [i.position for i in vehicles if not i.ID == self.ID]
        slow_case = range(self.position, self.position + self.speed + self.danger_zone)
        regular_case = range(self.position, self.position + self.speed + self.danger_zone + 1)
        acceleration_case = range(self.position, self.position + self.speed + self.danger_zone + 2)
        dz_cars = range(self.position, self.position + self.danger_zone + 1)

        for i in cars_position:
            if i in dz_cars:
                # никуда не сдвинусь
                return
            elif i in slow_case:
                self.slow()
                return
            elif i in regular_case:
                self.slow()
                self.position += self.speed
                return
            elif i in acceleration_case:
                self.position += self.speed
                return

        # если нет машин поблизости, ускоряемся и едем
        self.accelerate()
        self.position += self.speed

class TrafficSystemSimulator:
    def __init__(self, road):
        self.road = road
        self.road_render = list('▓' * self.road.length)

    def run_cycle(self):
        while self.road.vehicles:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Каждая машина принимает решение
            for vehicle in self.road.vehicles:
                vehicle.decide_action(self.road.vehicles)            

            for v in self.road.vehicles:
                if 0 <= v.position < self.road.length:
                    self.road_render[v.position] = '#'

            print('-' * self.road.length)
            print(''.join(self.road_render))
            print('-' * self.road.length)
            time.sleep(1)

            for v in self.road.vehicles:
                if 0 <= v.position < self.road.length:
                    self.road_render[v.position] = '▓'

            # Удаление машин, вышедших за пределы дороги
            self.road.vehicles = [v for v in self.road.vehicles if v.position < self.road.length]
