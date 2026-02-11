import time
import sys
import threading
from datetime import datetime
import os

if os.name == 'nt':
    import msvcrt
else:
    import select

class TerminalApp:
    def __init__(self):
        self.text_vault = "Начальный текст.\n"
        self.start_time = time.time()
        self.running = True
        self.input_lock = threading.Lock()
        self.input_buffer = ""

    def move_to_line(self, line):
        print(f"\033[{line};1H", end='', flush=True)

    def clear_line(self):
        print("\033[2K", end='', flush=True)

    def update_display(self):
        while self.running:
            try:
                # Строка 1: текущее время
                self.move_to_line(1)
                self.clear_line()
                print(datetime.now().strftime("%H:%M:%S"), end='', flush=True)

                # Строка 2: таймер
                self.move_to_line(2)
                self.clear_line()
                elapsed = int(time.time() - self.start_time)
                print(f"{elapsed // 60:02d}:{elapsed % 60:02d}", end='', flush=True)

                # Строка 3: text_vault (первые 80 символов)
                self.move_to_line(3)
                self.clear_line()
                display_text = self.text_vault[:80] + "..." if len(self.text_vault) > 80 else self.text_vault
                print(display_text.rstrip(), end='', flush=True)

                # Строка 4: ввод
                self.move_to_line(4)
                self.clear_line()
                print("Ввод: " + self.input_buffer, end='', flush=True)

            except Exception:
                pass
            time.sleep(0.5)

    def get_input(self):
        self.input_buffer = ""
        while self.running:
            if os.name == 'nt':  # Windows
                if msvcrt.kbhit():
                    char = msvcrt.getch().decode('utf-8', errors='ignore')
                    if ord(char) == 13 or char == '\r':  # Enter
                        with self.input_lock:
                            if self.input_buffer.strip():
                                self.text_vault += self.input_buffer + "\n"
                            self.input_buffer = ""
                    elif ord(char) == 3:  # Ctrl+C
                        self.running = False
                    else:
                        self.input_buffer += char
            else:  # Unix: неблокирующий select каждые 0.05с
                ready, _, _ = select.select([sys.stdin], [], [], 0.05)
                if ready:
                    char = sys.stdin.read(1)
                    if char == '\n':
                        with self.input_lock:
                            if self.input_buffer.strip():
                                self.text_vault += self.input_buffer + "\n"
                            self.input_buffer = ""
                    elif char == '\x03':  # Ctrl+C
                        self.running = False
                    else:
                        self.input_buffer += char
            time.sleep(0.05)

    def run(self):
        try:
            # Очистить экран и скрыть курсор
            print("\033[2J\033[H\033[?25l", end='', flush=True)

            display_thread = threading.Thread(target=self.update_display, daemon=True)
            input_thread = threading.Thread(target=self.get_input, daemon=True)

            display_thread.start()
            input_thread.start()

            input_thread.join()  # Ждём ввод
        except KeyboardInterrupt:
            self.running = False
        finally:
            self.running = False
            print("\033[?25h\033[2J\033[H", end='', flush=True)  # Показать курсор, очистить
            print("Программа завершена. text_vault:\n" + self.text_vault[:200])

if __name__ == "__main__":
    app = TerminalApp()
    app.run()
