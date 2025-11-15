import time
import os
import uuid
from abc import ABC, abstractmethod

# road_len = 20
# road_left = list('0' * road_len)
# road_right = list('0' * road_len)
# car = '#'
# def road_sim():
#     for i in range(len(road_right)):
#         road_right[i] = car
#         print(*road_right)
#         road_right[i] = '0'
#         time.sleep(1)
#         os.system('cls' if os.name == 'nt' else 'clear')

# содержит
class Road:
    def __init__(self, length=20):
        self.length = length
        self.dir_left = list('░'*length)
        self.dir_right = list('░'*length)
        self.vehicles = []

class Vehicle(ABC):
    def __init__(self, position, speed, speed_limit):
        self.ID = uuid.uuid4()
        self.position = position
        self.speed = speed
        self.speed_limit = speed_limit
    def accelerate(self):
        self.speed = self.speed + 1
        return self.speed
    def slow(self):
        self.speed = self.speed - 1
        return self.speed
    @abstractmethod
    def decide_action(self):
        pass

class Car(Vehicle):
    def decide_action(self):
        return 1

# управляет трафиком
class TrafficFlowSimulator:
    def __init__(self, road):
        self.road = road
    def add_vehicle(self, vehicle):
        self.road.vehicles.append(vehicle)
    def run_cycle(self):
        self.road.vehicles.pop(0)
        for i in range(len(self.road.vehicles)):
            print(self.road.vehicles[i])


        # for i in range(self.road.length):
        #     os.system('cls' if os.name == 'nt' else 'clear')
        #     # дорога
        #     print('-' * self.road.length, sep='')
        #     print(*self.road.dir_left[::-1], sep='')
        #     print('- ' * int(self.road.length / 2), sep='')
        #     print(*self.road.dir_right[::-1], sep='')
        #     print('-' * self.road.length, sep='')
        #     time.sleep(0.1)
# --------------------
# ░░░░░░░░░░░░░░░░░░░░
# - - - - - - - - - -
# ░░░░░░░░░░░░░░░░░░░░
# --------------------