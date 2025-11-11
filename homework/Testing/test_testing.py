import sys
sys.path.append('')
import testing

# тест букав
def test_palindrome_sting():
    assert testing.ispalindrome('asdfdsa') == True
def test_not_case_sensetive():
    assert testing.ispalindrome('AsdfDsa') == True
# тест цифр
def test_digits():
    assert testing.ispalindrome('123321') == True
# не палиндром
def not_palindrome():
    assert testing.ispalindrome('1234') == False

