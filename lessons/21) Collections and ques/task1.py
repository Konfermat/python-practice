from asyncio import current_task
from collections import deque

class TaskQueue:
    def __init__(self, max_len=5):
        self.max_len = max_len
        self.queue: deque = deque(maxlen=max_len)

    def add_task(self, task):
        self.queue.append(task)
        if len(self.queue) == self.max_len and self.max_len > 0:
            print('возможно старая задача была удалена')

    def get_task(self):
        return list(self.queue)

print('тестирование')

task_manager = TaskQueue()
for i in range(1, 12):
    task_manager.add_task(f'задача {i}')
current_tasks_1 = task_manager.get_task()
print(current_tasks_1)
print(len(current_tasks_1))






