import asyncio
import logging
from asyncio import timeout
from threading import Thread, Event as ThreadEvent
from multiprocessing import Queue, Event as MP_Event
from config import setup_logging
from file_monitor import FileMonitor
from task_manager import TaskManager
from category_analyzer import CategoryAnalyzer

import signal
import sys

class TaskPlanner:
    def __init__(self):
        setup_logging()
        self.logger = logging.getLogger(__name__)
        self.shutdown_event = MP_Event()
        self.analyzer_in_queue = Queue()
        self.analyzer_out_queue = Queue()

        self.file_event = asyncio.Event()

        self.file_monitor = None
        self.task_manager = None
        self.analyzer_process = None

    def setup_signal_handlers(self):
        '''настройка обработчика сигналов (для корректного завершения)'''
        def signal_handler(sig, frame):
            '''обработчик сигналов'''
            self.logger.info(f'Получил сигнал {sig}. Завершение работы')
            self.shutdown()
            sys.exit(0)
        signal.signal(signal.SIGINT, signal_handler) # ctrl+c
        signal.signal(signal.SIGTERM, signal_handler) #завершение


    def shutdown(self):
        self.logger.info('Завершение работы планировщика')
        if self.task_manager:
            self.task_manager.stop()
        if self.file_monitor:
            self.file_monitor.stop()
            self.file_monitor.join(timeout=5)
        if self.analyzer_process and self.analyzer_process.is_alive():
            self.analyzer_in_queue.put(None)
            self.analyzer_process.join(timeout=5)

            if self.analyzer_process.is_alive():
                self.analyzer_process.termintate()

        self.logger.info('Все компонениы установлены')


