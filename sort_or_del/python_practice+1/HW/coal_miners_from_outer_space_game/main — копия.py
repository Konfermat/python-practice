from threading import Thread
import time
import threading


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

text = 'Text with data: ?\nAnoter text: ?'
buffer = ''
text_to_add = ''

print(text)


фывафыав
Введите текст: *

фывафыав
Введите текст: йцук*

фывафыав
йцук
Введите текст: *