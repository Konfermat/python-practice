from trafic_system_sim import *

if __name__ == '__main__':
    road1 = Road()
    car1 = Car(0, 1, 3)
    car2 = Car(1, 1, 3)

    simulation = TrafficFlowSimulator(road1)
    simulation.add_vehicle(car1)
    simulation.add_vehicle(car2)

    simulation.run_cycle()
