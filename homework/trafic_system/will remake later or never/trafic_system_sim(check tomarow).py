import time
import os
from abc import ABC, abstractmethod
import uuid
print('hello')



class Road:
    def __init__(self, length = 10, direction = 'right'):
        self.length = length
        self.direction = direction
        self.vehicles = []
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        
class Vehicle(ABC):
    def __init__(self, position = 0, speed = 1, max_speed = 4, danger_zone=1):
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
    def decide_action(self, vehicles):
        # позиции остальных машин
        cars_position = [i.position for i in vehicles if not i.ID == self.ID]
        # отрезок с если замедлюсь
        slow_case = range(self.position, self.position + self.speed + self.danger_zone)
        # проеду как обычно
        regular_case = range(self.position, self.position + self.speed + self.danger_zone + 1)
        # отрезок под ускорением
        acceleration_case = range(self.position, self.position + self.speed + self.danger_zone + 2)
        # машины в опасной зоне
        dz_cars = range(self.position, self.position + self.danger_zone + 1)
        #
        for i in cars_position:
            # если перед тобой машина
            if i in dz_cars:
                # никуда не сдвинусь
                break
            # остановить и сбавить cорость
            elif i in slow_case:
                self.slow()
                break
            # сбавить проехать
            elif i in regular_case:
                self.slow()
                self.position += self.speed
                break
            # едь как обычно
            elif i in acceleration_case:
                self.position += self.speed
                break
            # едь с ускорением
            else:
                self.accelerate()
                self.position += self.speed
                break

class TrafficSystemSimulator:
    def __init__(self, road):
        self.road = road
        self.road_render = list('▓' * self.road.length)

    def run_cycle(self):
        
        # пока на дороге есть машины
        while not self.road.vehicles == []:
            # чистка терминала
            os.system('cls' if os.name == 'nt' else 'clear')

            # поместить машины в рендер
            for i in self.road.vehicles:
                self.road_render[i.position] = '#' 
                
            # цикл рендерит дорогу
            print('-'*self.road.length, sep='')
            print(*self.road_render, sep='')
            print('- '*self.road.length, sep='')
            print(*self.road_render, sep='')
            print('-'*self.road.length, sep='')
            time.sleep(0.1)
            
            # убрать машины из рендера
            for i in self.road.vehicles:
                self.road_render[i.position] = '▓' 
            
            # каждая машина принимает решение увеличить или замедлить скорость
            for vehicle in self.road.vehicles:
                vehicle.decide_action(self.road.vehicles)
            for i in range(len(self.road.vehicles)):
                self.road.vehicles[i].decide_action(self.road.vehicles)
            
            # удаление машины если вышла за пределы
            for i in range(len(self.road.vehicles)):
                if self.road.vehicles[i].position > self.road.length:
                    self.road.vehicles.pop(i)
    def test(self):
        print(self.road.vehicles)

def main():
    car1 = Car()
    car2 = Car()
    road = Road()
    road.add_vehicle(car1)
    tss = TrafficSystemSimulator(road)
    tss.run_cycle()
    # tss.test()
main()