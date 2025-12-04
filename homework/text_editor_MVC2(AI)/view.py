import sys
sys.path.append('')
from datetime import datetime

# ===== View =====
class VersionView:
    @staticmethod
    def show_message(msg):
        print(msg)

    @staticmethod
    def input_prompt(msg):
        return input(msg)

    @staticmethod
    def show_file_content(content):
        print("\nСодержимое файла:\n")
        print(content)

    @staticmethod
    def show_versions(history):
        if not history:
            print("История версий пуста.")
            return
        print("История версий:")
        for i, version in enumerate(history):
            print(f"{i}. {version['timestamp']} ({version['size']} символов)")

    @staticmethod
    def input_multiline():
        print("Введите новый текст файла (конец ввода - пустая строка):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        return "\n".join(lines)