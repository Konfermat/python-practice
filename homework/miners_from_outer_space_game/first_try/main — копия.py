from threading import Thread
import time
import os

class Mine(Thread):
    def __init__(self):
        super().__init__()
        res_amount = 0
        res_inc = 0
        tier = 1
        

class Clock(Thread):
    def __init__(self):
        self.mlp = 1
        self.clock_flag = False
        self.time_dif = 0
        self.restart = 424242_424242
        
        
    
    def start_clock(self):
        self.clock_flag = True
        self.time_dif = time.time()
        
        while self.clock_flag:
            os.system('cls' if os.name == 'nt' else 'clear')
            if (time.time() - self.time_dif) * self.mlp > self.restart:
                self.time_dif = time.time()
            print(time.strftime("%H:%M:%S", time.gmtime((time.time() - self.time_dif) * self.mlp)))
            print((time.time() - self.time_dif) * self.mlp)
            time.sleep(1)
        
    def stop_clock(self):
        self.clock_flag = False
        
class Timer:
    def __init__(self):
        pass

c1 = Clock()
c2 = Clock()
c2.mlp = 55

c2.start_clock()


