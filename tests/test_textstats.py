from textstats import count_chars, count_lines, count_words


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


def test_count_lines_empty():
    assert count_lines("") == 0


def test_count_lines_single_line():
    assert count_lines("a") == 1


def test_count_lines_ignores_one_trailing_newline():
    assert count_lines("a\n") == 1


def test_count_lines_multiple_lines():
    assert count_lines("a\nb") == 2


def test_count_lines_counts_blank_lines():
    assert count_lines("a\n\nb") == 3


def test_count_lines_only_newline():
    assert count_lines("\n") == 1


def test_count_lines_windows_newline():
    assert count_lines("a\r\nb") == 2
