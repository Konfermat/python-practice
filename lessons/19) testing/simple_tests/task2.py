import pytest
import string


def count_punct_marks(s: str) -> int:
    total_count = 0
    for sym in string.punctuation:
        total_count += s.count(sym)
    return total_count


def test_empty():
    assert count_punct_marks('') == 0

def test_no():
    assert count_punct_marks('Hello world') == 0

def test_single():
    assert count_punct_marks('Hello world!') == 1

def test_multiple():
    assert count_punct_marks('Hello, world! How are you?') == 3

def test_edge():
    assert count_punct_marks('!!!') == 3

def test_all():
    assert count_punct_marks('?') == 1
    