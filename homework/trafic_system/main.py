import sys
sys.path.append('')
import trafic_system_sim

if __name__ == '__main__':
    car1 = trafic_system_sim.Truck(0)
    car2 = trafic_system_sim.Car(1)
    road = trafic_system_sim.Road(20)
    road.add_vehicle(car1)
    road.add_vehicle(car2)
    tss = trafic_system_sim.TrafficSystemSimulator(road)
    tss.run_cycle()

