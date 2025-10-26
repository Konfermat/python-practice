import time
class FinancialDescriptor:

    def __init__(self, name: str, min_value: float, max_value: float, history: dict):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.history = history

