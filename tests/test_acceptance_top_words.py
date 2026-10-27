"""验收测试（第一批，公开）：top_words。由起草方事先编写，实现方不得修改或删除。"""

from textstats import top_words


def test_basic_counts_sorted_by_frequency():
    assert top_words("b a b c b a", 3) == [("b", 3), ("a", 2), ("c", 1)]


def test_case_insensitive_and_lowercased():
    assert top_words("Hello hello HELLO world", 2) == [("hello", 3), ("world", 1)]


def test_punctuation_is_separator():
    assert top_words("cat, dog. cat!", 2) == [("cat", 2), ("dog", 1)]


def test_ties_sorted_alphabetically():
    assert top_words("pear apple pear apple fig", 3) == [("apple", 2), ("pear", 2), ("fig", 1)]


def test_n_zero_returns_empty():
    assert top_words("a b c", 0) == []
