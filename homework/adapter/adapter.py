import sys
sys.path.append('')
from abc import ABC, abstractmethod

class OldFileLogger:
    def log_to_file(self, message, level):
        print(f'message: {message}, level: {level}')
    
class ConsolePrinter:
    def print_message(self, data):
        tmp = list(data.items())[0]
        print(f'dictionary content: key: {tmp[0]}, value: {tmp[1]}')

class LoggerInterface(ABC):
    def log(self, message, level):
        pass

class FileLoggerAdapter(LoggerInterface):
    def __init__(self, ofl):
        self.ofl = ofl
    def log(self, message, level):
        self.ofl.log_to_file(message, level)

class ConsoleAdapter(LoggerInterface):
    def __init__(self, console_printer):
        self.console_printer = console_printer
    def log(self, message, level):
        temp = {message: level}
        self.console_printer.print_message(temp)

