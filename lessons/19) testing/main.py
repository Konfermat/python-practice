'''
# pip install pytest
# pip list
import unittest


def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b

divide(5, 2)
divide(5, 0)
print('hello world')

# игнорирует assert если запуск с линукса
# python -o main.py
# cd name

class TestExample(unittest.TestCase): # Тоже с Test
    def test_addition(self): # имя всегда начинается с test
        # проверяет ожидаемое значение
        self.assertNotEqual(2 + 2, 4)
        self.assertTrue(True)
        self.assertFalse(True)
        # self.assertRaises(Exception, lambda: 2 + 2) # значение, функция, аргумент

    def test_divide(self):
        self.assertEqual(divide(divide(10, 2), 5)
        self.assertRaises(ZeroDivisionError, divide, 10, 0)

if __name__ == '__main__':
    unittest.main()
'''

import pytest
add = lambda x, y: x + y

def test_add():
    assert add(2, 3) == 4
    assert add(-1, 1) == 0

print('hello world')
 # python -m pytest main.py # запуск тестов

