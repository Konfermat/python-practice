import sys
sys.path.append('')

import os
import json
from datetime import datetime

VERSIONS_DIR = "versions_cli"

# ===== Model =====
class VersionModel:
    def __init__(self, filename):
        self.filename = filename if filename.endswith(".txt") else filename + ".txt"
        self.history_file = os.path.join(VERSIONS_DIR, f"{self.filename}_history.json")
        self.history = self.load_version_history()

    @staticmethod
    def create_versions_dir():
        if not os.path.exists(VERSIONS_DIR):
            os.makedirs(VERSIONS_DIR)

    def load_version_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, "r", encoding="utf-8") as file:
                return json.load(file)
        return []

    def save_version_history(self):
        with open(self.history_file, "w", encoding="utf-8") as file:
            json.dump(self.history, file, ensure_ascii=False, indent=2)

    def save_version(self, content):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        version_name = f"{self.filename}_{timestamp}.txt"
        version_path = os.path.join(VERSIONS_DIR, version_name)
        with open(version_path, "w", encoding="utf-8") as file:
            file.write(content)
        version_info = {
            "filename": version_name,
            "timestamp": timestamp,
            "size": len(content)
        }
        self.history.append(version_info)
        self.save_version_history()
        return version_info

    def read_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                return file.read()
        return None

    def write_file(self, content):
        with open(self.filename, "w", encoding="utf-8") as file:
            file.write(content)

    def restore_version(self, index):
        if 0 <= index < len(self.history):
            version_file = os.path.join(VERSIONS_DIR, self.history[index]["filename"])
            content = self._read_version_file(version_file)
            if content is not None:
                self.write_file(content)
                return True, self.history[index]["timestamp"]
            else:
                return False, "Файл версии не найден."
        return False, "Неверный индекс версии."

    @staticmethod
    def _read_version_file(path):
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as file:
                return file.read()
        return None




