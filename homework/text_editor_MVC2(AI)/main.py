import sys
sys.path.append('')

from model import VersionModel
from controller import VersionController
from view import VersionView

if __name__ == "__main__":
    filename = input("Введите имя файла (.txt): ").strip()
    model = VersionModel(filename)
    view = VersionView()
    controller = VersionController(model, view)
    controller.run()

