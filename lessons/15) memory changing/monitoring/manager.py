import os
import csv
from visuallizer import ConsoleVisualizer, ImageVisualizer
from metrics import CPUMetric, RAMMetric, DiskMetric, ResourceMetric
import time


class MonitorManager:

    def __init__(self):
        self.metrics = []

    def add_metric(self, metric):
        self.metrics.append(metric)

    def update_all_metrics(self):
        for metric in self.metrics:
            metric.update()

    def _clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_console(self):
        self._clear_console()

        for metric in self.metrics:
            if isinstance(metric, ResourceMetric):
                ConsoleVisualizer.draw_bar(metric.value, metric.name)

    def run_console(self, interval: int = 1):
        try:
            while True:
                time.sleep(interval)
                self.update_all_metrics()
                self.display_console()
        except KeyboardInterrupt:
            print(f'/n/nМониторинг остановлен')

    def generate_image_report(self):
        self.update_all_metrics()
        self.display_console()
        visualizer = ImageVisualizer()
        visualizer.create_report(self.metrics)


