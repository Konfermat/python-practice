from threading import Thread
import time
import threading
from concurrent.futures import ThreadPoolExecutor


class Clock(Thread):
    def __init__(self):
        self.clock_flag = False
        self.multiplier = 1
        self.restart = 43200 #12 hours
        self.start = 0
        self.elapsed = 0
        self.oposite_meridiem = "PM"
        self.curr_meridiem = "AM"
    def get_time(self):
        return (time.perf_counter() - self.start) * self.multiplier

    def start_clock(self):
        self.clock_flag = True
        self.start = time.perf_counter()
        while self.clock_flag:
            self.elapsed = self.get_time()
            if self.elapsed > self.restart:
                self.curr_meridiem, self.oposite_meridiem = self.oposite_meridiem, self.curr_meridiem,
                self.start_clock()
            print(f'\r{self.curr_meridiem} {time.strftime('%H:%M:%S', time.gmtime(self.elapsed))}', end='')
            time.sleep(1/self.multiplier)
    def stop_clock(self):
        self.clock_flag = False
        print()

# Тест
#c2 = Clock()
#c2.start_clock()

text = 'Text one,?Text two,?Text three,?Text forth,?Text fifth.'.split('?')

esc_seq = '\x1b[1A\x1b[2K'        

def get_time(multiplier):
    print(time.strftime('%H:%M:%S', time.localtime(time.time()*multiplier)))

def get_data():
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.submit(get_time, 1)
        executor.submit(get_time, 2)
        executor.submit(get_time, 3)
        

while True:
    print(esc_seq*3+f'\x1b[{8}D', end='')
    get_data()
    


