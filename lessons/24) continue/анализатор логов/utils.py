import re
from functools import wraps
import time
import datetime

LOG_PATTERN = re.compile(
    r'^(\S+) \S+ \S+ \[(.+)\] \"(\S+) (\S+) (\S+)\" (\d+) (\S+) \"([^\"]*)\" \"([^\"]*)\"'
)
# порог для тяжелых запросов
HEAVY_REQUEST = 1024

# 142.226.230.45 - - [27/Oct/2025:00:00:00 +0300] "GET /contact HTTP/2.0" 200 2773 "https://myers.net/" "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/25.0.882.0 Safari/533.2"
class StatusCodeValidator:
    def __init__(self, default_value=0):
        self.name = None
        self.default_value = default_value

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, self.default_value)

    def __set__(self, instance, value):
        try:
            int_value = int(value)
            if 100 <= int_value <= 599:
                instance.__dict__[self.name] = int_value
            else:
                instance.__dict__[self.name] = self.default_value
        except (ValueError, TypeError):
            instance.__dict__[self.name] = self.default_value

def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # первый аргумент 'nj self
        self = args[0]
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        self.analysis_time = end_time - start_time
        return result
    return wrapper

class LogEntry:
    status_code = StatusCodeValidator()

    def __init__(self, ip, timestamp, method, url, protocol, status_code, size, referrer, user_agent):
        self.ip = ip
        #[27 / Oct / 2025: 00:00: 06 + 0300]
        try:
            self.timestamp = datetime.datetime.strptime(timestamp.split(' ')[0], '%d/%b/%Y:%H:%M:%:%S')
        except ValueError:
            self.timestamp = None
        self.method = method
        self.url = url
        self.protocol = protocol
        self.status_code = status_code
        try:
            self.size = int(size)
        except ValueError:
            self.size = 0
        # рефер откуда запрос пришел
        self.referrer = referrer
        self.user_agent = user_agent

    @property
    def full_request(self):
        # предоставление запроса для вывода в отчет
        return f'{self.method} {self.url}'

    def __str__(self):
        return f'LogEntry(ip="{self.ip}", status="{self.status_code}", size="{self.size}", url="{self.url}")'

def log_parser(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = LOG_PATTERN.match(line)
                if match:
                    data = match.groups() #  кортеж с найдеными группами
                    yield LogEntry(*data) # разспаковка в отделльные элементы

    except FileNotFoundError:
        return
    except Exception as e:
        print(f'[ERROR] {e}')
        return



# with open('access.log', 'r') as log:
#     iterrator = iter(log)
#     for line in iterrator:
#         line = line.strip()
#         match = LOG_PATTERN.match(line)
#         print(match)
