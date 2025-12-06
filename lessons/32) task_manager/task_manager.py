import logging
import asyncio
from encodings import search_function

from multiprocessing import Queue
from datetime import datetime, timedelta
from openpyxl import load_workbook
from openpyxl.utils.exceptions import InvalidFileException
from pathlib import Path
import time

# библиотека для звука
from config import EXCEL_FILE, COLUMNS, STATUS_PENDING, STATUS_DONE, NOTIFY_FILE, CATEGORIES

logger = logging.getLogger(__name__)

class TaskManager:
    def __init__(self, file_event: asyncio.Event, analyzer_in_queue: Queue, analyzer_out_queue: Queue):
        self.tasks = [] # список asyncio.Task
        self.file_event = file_event # Event at FileMonitor
        self.analyzer_in_queue = analyzer_in_queue
        self.analyzer_out_queue = analyzer_out_queue

    def _play_sound(self, file: Path):
        pass

    async def _async_wait_and_notify(self, task_data: dict):
        task_time_str = task_data[COLUMNS['TIME']]
        task_desc = task_data[COLUMNS['TASK']]
        task_category = task_data[COLUMNS['CATEGORY']]
        row_index = task_data['row_index']
        try:
            target_time = datetime.strptime(task_time_str, '%H:%M').time()
            now = datetime.now()
            target_datetime = datetime.combine(now.date(), target_time)
            if target_datetime < now:
                target_datetime += timedelta(days=1)
            wait_seconds = (target_datetime - now).total_seconds()
            logger.info(f'Задача {task_desc} будет ждать {round(wait_seconds)} секунд до {target_time.isoformat(timespec='minutes')}.')
            await asyncio.sleep(wait_seconds)
            notify_msg = (
                f'НАПОМИНАНИЕ: [{task_time_str}] {task_category}. {task_desc}'
            )
            print('\n'+'-'*30)
            print(notify_msg)
            print('-'*30+'\n')
            logger.info(f'Отправка уведомления о задаче  {notify_msg}')
            sound_path = Path(NOTIFY_FILE)
            if sound_path.exists():
                await asyncio.to_thread(self._play_sound, sound_path)
                logger.info('Воспроизведен звуковой сигнал')
            else:
                logger.warning(f'Звуковой файл {NOTIFY_FILE} не найден')
            await asyncio.to_thread(self._update_status_excel, row_index, STATUS_DONE)
        except asyncio.CancelledError:
            logger.debug(f'Ассинхронное ожидание задачи {task_desc} отменено')
            raise # перебрасываем ошибку для корректной обработки отмены
        except Exception as e:
            logger.error(f'Ошибка в асинхронном ожидании задачи {task_desc}: {e}')

    def _read_task_excel(self)->list:
        pass

    def _update_category_excel(self, row_index, new_status):
        pass

    def _update_status_excel(self, row, status):
        pass

    def main_loop(self):
        pass

    def stop(self):
        pass