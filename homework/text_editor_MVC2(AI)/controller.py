import sys
sys.path.append('')

from model import VersionModel
from view import VersionView


# ===== Controller =====
class VersionController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        VersionModel.create_versions_dir()
        self.view.show_message("Простой текстовый редактор (консольный)\n")

        while True:
            self.view.show_message("\nДоступные команды:")
            self.view.show_message("1 - Просмотр содержимого файла")
            self.view.show_message("2 - Редактировать файл")
            self.view.show_message("3 - Сохранить изменения и создать версию")
            self.view.show_message("4 - Показать историю версий")
            self.view.show_message("5 - Восстановить версию")
            self.view.show_message("6 - Новый файл")
            self.view.show_message("0 - Выход")
            cmd = self.view.input_prompt("Введите команду: ").strip()

            if cmd == "1":
                content = self.model.read_file()
                if content is None:
                    self.view.show_message("Файл не найден или пуст.")
                else:
                    self.view.show_file_content(content)

            elif cmd == "2":
                new_content = self.view.input_multiline()
                self.model.write_file(new_content)
                self.view.show_message("Файл отредактирован, не забудьте сохранить, чтобы создать версию.")

            elif cmd == "3":
                content = self.model.read_file()
                if content is None:
                    self.view.show_message("Файл пустой, нечего сохранять.")
                else:
                    version_info = self.model.save_version(content)
                    self.view.show_message("Файл сохранён и версия создана.")

            elif cmd == "4":
                self.view.show_versions(self.model.history)

            elif cmd == "5":
                self.view.show_versions(self.model.history)
                if self.model.history:
                    ix = self.view.input_prompt("Введите номер версии для восстановления: ").strip()
                    if ix.isdigit():
                        success, msg = self.model.restore_version(int(ix))
                        if success:
                            self.view.show_message(f"Версия {msg} восстановлена в файл {self.model.filename}.")
                        else:
                            self.view.show_message(f"Ошибка: {msg}")
                    else:
                        self.view.show_message("Неверный ввод.")

            elif cmd == "6":
                filename = self.view.input_prompt("Введите имя нового файла (.txt): ").strip()
                self.model = VersionModel(filename)
                self.view.show_message(f"Создан новый файл: {self.model.filename}")

            elif cmd == "0":
                self.view.show_message("Выход...")
                break

            else:
                self.view.show_message("Неизвестная команда, попробуйте снова.")
