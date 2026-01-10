import threading
import time
import random
from collections import defaultdict

class Mine(threading.Thread):
    def __init__(self, name, resource, base_rate=5, daemon=True):
        super().__init__(daemon=daemon)
        self.name = name
        self.resource = resource
        self.rate = base_rate
        self.level = 1
        self.running = True
        self.broken = False
        self.lock = threading.Lock()
        self.storage = defaultdict(int)  # Глобальный склад через shared dict

    def run(self):
        while self.running:
            with self.lock:
                if self.broken:
                    time.sleep(1)
                    continue
                self.storage[self.resource] += self.rate
                if random.random() < 0.01:  # Поломка ~1/100 сек
                    self.broken = True
            time.sleep(1)

    def upgrade(self, cost=1000):
        with self.lock:
            if not self.broken and self.storage['money'] >= cost:
                self.storage['money'] -= cost
                self.rate += 3
                self.level += 1
                time.sleep(5)  # Блокировка

    def repair(self, parts=10):
        with self.lock:
            if self.broken and self.storage['Parts'] >= parts:
                self.storage['Parts'] -= parts
                self.broken = False
