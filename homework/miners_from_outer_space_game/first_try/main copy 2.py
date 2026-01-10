from threading import Thread
import time

class Clock(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.clock_flag = False
        self.multiplier = 100
        self.time_dif = 0
        self.restart = 424242_424242
    
    def run(self):
        self.clock_flag = True
        self.time_dif = time.time()
        
        last_time = 0
        
        while self.clock_flag:
            elapsed = (time.time() - self.time_dif) * self.multiplier
            if elapsed > self.restart:
                self.time_dif = time.time()
                elapsed = 0
            
            current_time = int(elapsed * 5)  # 0.2 сек обновление
            if abs(current_time - last_time) >= 1:
                timer_str = time.strftime("%H:%M:%S", time.gmtime(elapsed))
                print(f"\r{timer_str}", end='', flush=True)  # Первый раз тоже \r
                last_time = current_time
            
            time.sleep(1/self.multiplier)
        
        print()  # После остановки

    
    def stop_clock(self):
        self.clock_flag = False

class TextStream(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.text = ''

    def run(self):
        while True:
            self.text += input(' ')

# Тест
c1 = Clock()
t1 = TextStream()
c1.multiplier = 1000

c1.start()
t1.start()

c1.join()
t1.join()
print(input())
