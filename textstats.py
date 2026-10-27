"""练手项目：简单的文本统计工具。"""


def count_chars(text: str) -> int:
    """返回字符数（不含空白字符）。"""
    return sum(1 for ch in text if not ch.isspace())


def count_words(text: str) -> int:
    """返回以空白分隔的英文单词数。"""
    return len(text.split())


def count_lines(text: str) -> int:
    """返回文本的行数。"""
    return len(text.splitlines())
