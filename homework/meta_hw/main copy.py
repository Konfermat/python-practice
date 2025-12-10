class DocumentationError(TypeError):
    """Пользовательское исключение для отсутствия документации."""
    pass

class DocstringEnforcer(type):
    """
    Метакласс, который принудительно требует docstring у всех создаваемых классов.
    
    Проверяет наличие непустого __doc__ атрибута. Если документация отсутствует,
    вызывает DocumentationError.
    """
    def __new__(mcs, name, bases, namespace, **kwargs):
        # Получаем docstring из namespace
        docstring = namespace.get('__doc__')
        
        # Проверяем наличие docstring
        if docstring is None or docstring.strip() == "":
            raise DocumentationError(
                f"Класс '{name}' должен иметь docstring! "
                f"Найден: {repr(docstring)}"
            )
        
        # Создаем класс, если проверка пройдена
        return super().__new__(mcs, name, bases, namespace, **kwargs)


# Тестовые классы

class DocumentedClass(metaclass=DocstringEnforcer):
    """
    Пример класса с корректной документацией.
    
    Этот класс успешно создается, так как имеет docstring.
    """
    def hello(self):
        return "Привет из документированного класса!"

# Этот класс вызовет ошибку при определении:
# class UndocumentedClass(metaclass=DocstringEnforcer):
#     def hello(self):
#         return "Привет!"

# Демонстрация работы
if __name__ == "__main__":
    print("Создание DocumentedClass...")
    try:
        doc_class = DocumentedClass()
        print("✓ DocumentedClass создан успешно!")
        print(f"Docstring: {DocumentedClass.__doc__.strip()[:50]}...")
    except DocumentationError as e:
        print(f"✗ Ошибка: {e}")
    
    print("\nПопытка создания UndocumentedClass...")
    try:
        # Раскомментируйте следующую строку для тестирования ошибки
        # UndocumentedClass()
        print("Для теста ошибки раскомментируйте определение UndocumentedClass")
    except DocumentationError as e:
        print(f"✗ Ошибка (ожидалась): {e}")
