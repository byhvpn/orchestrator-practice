from textstats import count_chars, count_words


def test_count_chars_ignores_whitespace():
    assert count_chars("a b\tc\n") == 3


def test_count_chars_chinese():
    assert count_chars("你好 世界") == 4


def test_count_chars_empty():
    assert count_chars("") == 0


def test_count_words_basic():
    assert count_words("hello  world\nagain") == 3


def test_count_words_empty():
    assert count_words("   ") == 0
