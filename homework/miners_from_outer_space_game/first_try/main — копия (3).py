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
        self.clock_flag = False
        self.multiplier = 10
        self.time_dif = 0
        self.restart = 424242_424242
    
    def start_clock(self):
        self.clock_flag = True
        self.time_dif = time.time()
        
        # Проверяем поддержку ANSI правильно
        supports_ansi = False
        try:
            import colorama
            colorama.init()  # Инициализирует ANSI в Windows
            supports_ansi = True
        except ImportError:
            supports_ansi = os.name != 'nt'
        
        print("Таймер запущен:")
        first_run = True
        last_time = 0
        
        while self.clock_flag:
            elapsed = (time.time() - self.time_dif) * self.multiplier
            
            # СБРОС только при переполнении
            if elapsed > self.restart:
                self.time_dif = time.time()
                elapsed = 0
            
            # Обновляем ВИЗУАЛЬНО только раз в 100мс (10 Гц)
            current_time = int(elapsed * 10)  # 0.1 сек точность
            if abs(current_time - last_time) >= 1 or first_run:
                timer_str = time.strftime("%H:%M:%S", time.gmtime(elapsed))
                
                if first_run:
                    print(timer_str)
                    first_run = False
                elif supports_ansi:
                    # ANSI без flush и мигания
                    print(f'\033[1A\033[2K\r{timer_str}', end='\r')
                else:
                    # Fallback с минимальным миганием
                    print(f'\rТаймер: {timer_str}', end='', flush=True)
                
                last_time = current_time
            
            time.sleep(1/self.multiplier)  # Вычисления остаются быстрыми

    
    def stop_clock(self):
        self.clock_flag = False


# Тестирование
if __name__ == "__main__":
    c1 = Clock()
    c2 = Clock()
    
    print("Запуск таймера c2:")
    c2.start_clock()
    
