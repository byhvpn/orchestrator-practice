"""验收测试（第二批，PR 开出后追加）：top_words。规则均来自任务描述，实现方不得修改或删除。"""

from textstats import top_words


def test_apostrophe_between_letters_is_part_of_word():
    assert top_words("don't don't do", 2) == [("don't", 2), ("do", 1)]


def test_apostrophe_not_between_letters_is_separator():
    assert top_words("'quoted' dogs' quoted", 2) == [("quoted", 2), ("dogs", 1)]


def test_multiple_inner_apostrophes():
    assert top_words("rock'n'roll", 1) == [("rock'n'roll", 1)]


def test_digits_are_separators():
    assert top_words("abc123abc 42", 5) == [("abc", 2)]


def test_non_english_characters_are_separators():
    assert top_words("hello世界hello café", 5) == [("hello", 2), ("caf", 1)]


def test_underscore_is_separator():
    assert top_words("snake_case snake", 5) == [("snake", 2), ("case", 1)]


def test_negative_n_returns_empty():
    assert top_words("a b", -1) == []


def test_n_larger_than_unique_words_returns_all():
    assert top_words("b a", 10) == [("a", 1), ("b", 1)]


def test_empty_text():
    assert top_words("", 3) == []


def test_three_way_tie_alphabetical_after_higher_count():
    assert top_words("z y x z", 4) == [("z", 2), ("x", 1), ("y", 1)]
