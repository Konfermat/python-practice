import os
import sys
from metrics import CPUMetric, RAMMetric, DiskMetric, ResourceMetric
from manager import MonitorManager


def main():
    manager = MonitorManager()
    manager.add_metric(CPUMetric())
    manager.add_metric(RAMMetric())

    root_path = '/'
    if sys.platform == 'win32':
        root_path = os.getenv('SystemDrive', 'C:') + '\\'
    manager.add_metric(DiskMetric(path=root_path))

    while True:
        print('\nВыберите действие: ')
        print('1. Мониторинг в реальном времени')
        print('2. Сгенерировать отчет')
        print('3. Выйти')
        choice = int(input())
        if choice == 1:
            manager.run_console()
        elif choice == 2:
            manager.generate_image_report()
        elif choice == 3:
            break
        else:
            print('Неверный ввод')

    manager.run_console()

if __name__ == '__main__':
    main()