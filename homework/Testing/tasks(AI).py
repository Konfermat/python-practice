def is_palindrome(s):
    s = s.lower()  # игнорируем регистр
    return s == s[::-1]

def word_count(s):
    s = s.lower()
    words = s.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count


# Тесты для is_palindrome()
assert is_palindrome("Level") == True  # палиндром из букв
assert is_palindrome("12321") == True  # палиндром из цифр
assert is_palindrome("Python") == False  # не палиндром

# Тесты для word_count()
assert word_count("Hello hello world") == {"hello": 2, "world": 1}  # корректный подсчёт, игнор регистра
assert word_count("") == {}  # пустая строка возвращает пустой словарь

print("Все тесты успешно пройдены!")