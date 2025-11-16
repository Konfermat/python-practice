import time
import os
import uuid
from abc import ABC, abstractmethod

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
    def decide_action(self, road):
        pass

class Car(Vehicle):
    def decide_action(self, road):
        p = self.position
        r_p = []

        # for i in range(len(road.vehicles)):
        #     road.dir_right[road.vehicles[i].position] = '░'

class TrafficFlowSimulator:
    def __init__(self, road):
        self.road = road
    def add_vehicle(self, vehicle):
        self.road.vehicles.append(vehicle)
    def run_cycle(self):





        for i in range(self.road.length):
            os.system('cls' if os.name == 'nt' else 'clear')

            for i in range(len(self.road.vehicles)):
                self.road.vehicles[i].decide_action(self.road)
                self.road.dir_right[self.road.vehicles[i].position] = '#'

            # дорога
            print('-' * self.road.length, sep='')
            print(*self.road.dir_left[::-1], sep='')
            print('- ' * int(self.road.length / 2), sep='')
            print(*self.road.dir_right, sep='')
            print('-' * self.road.length, sep='')

            for i in range(len(self.road.vehicles)):
                self.road.dir_right[self.road.vehicles[i].position] = '░'

            time.sleep(0.1)


# --------------------
# ░░░░░░░░░░░░░░░░░░░░
# - - - - - - - - - -
# ░░░░░░░░░░░░░░░░░░░░
# --------------------