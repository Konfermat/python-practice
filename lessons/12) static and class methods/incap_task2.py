import time
import random
# print(time.time())

class IDGenerator:
    @staticmethod
    def generate_id(server_number):
        timestamp = int(time.time())
        random_el = random.randint(1, 1000)
        return f'{server_number}-{timestamp}-{random_el}'

    @staticmethod
    def is_valid_id(id):
        parts = id.split('-')
        if len(parts) != 3:
            return False

        # server check
        server_number, timestamp, random_el = parts
        if not server_number.isdigit() or not timestamp.isdigit() or not random_el.isdigit():
            return False
        if int(server_number) < 1 or int(server_number) > 1000:
            return False

        #timestamp check
        if int(timestamp) <= 0 or int(timestamp) > int(time.time()):
            return False
        return True

    @staticmethod
    def generate_ids(base_size, server_number):
        return [IDGenerator.generate_id(server_number) for _ in range(base_size)]


id = IDGenerator.generate_id(1)
print(id)

is_valid = IDGenerator.is_valid_id(id)
print(is_valid)

ids = IDGenerator.generate_ids(10, 5)
print(ids)

