import logging
from multiprocessing import Process, Queue
from config import CATEGORIES, CATEGORY_KEYWORDS
import time
logger = logging.getLogger(__name__)
# с телеграм ботами маст хев бтв

class CategoryAnalyzer(Process):
    def __init__(self, input_queue: Queue, output_queue: Queue):
        super().__init__()
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.name = 'AnalyzerProcess'
        self.daemon = True

    def analyze_task(self, task_desc: str)->str:
        task_lower = task_desc.lower()
        for category, keywords in CATEGORY_KEYWORDS.items():
            for keyword in keywords:
                if keyword in task_lower:
                    time.sleep(0.2)
                    return category
        return 'Не определена'

    def run(self):
        logger.info(f'Процесс Анализатор запущен и ожидает задачи в очереди')
        while True:
            try:
                task_data = self.input_queue.get() # блокирующее ожидание
                # task_data (row_index, task_desc)
                if task_data is None:
                    logger.info('Получен сигнал о завершении. Процесс Анализатор завершает работу.')
                    break
                row_index, task_desc = task_data
                logger.info(
                    f'Задача "{task_desc}" (строка {row_index}) передача в Процесс для анализа'
                )
                new_category = self.analyze_task(task_desc)
                logger.info(f'Процесс определил Категорию для задачи "{task_desc}": {new_category}')
                self.output_queue.put((row_index, new_category))
            except KeyboardInterrupt:
                break
            except Exception as e:
                logger.error(f'Ошибка в Процесе-Анализаторе: {e}')


