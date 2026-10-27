"""练手项目：简单的文本统计工具。"""


import re
from collections import Counter


def count_chars(text: str) -> int:
    """返回字符数（不含空白字符）。"""
    return sum(1 for ch in text if not ch.isspace())


def count_words(text: str) -> int:
    """返回以空白分隔的英文单词数。"""
    return len(text.split())


def count_lines(text: str) -> int:
    """返回文本的行数。"""
    return len(text.splitlines())


_HANZI_RANGES = (
    (0x3400, 0x4DBF),
    (0x4E00, 0x9FFF),
    (0xF900, 0xFAFF),
    (0x20000, 0x2A6DF),
    (0x2A700, 0x2B73F),
    (0x2B740, 0x2B81F),
    (0x2B820, 0x2CEAF),
    (0x2CEB0, 0x2EBEF),
    (0x2EBF0, 0x2EE5F),
    (0x2F800, 0x2FA1F),
    (0x30000, 0x3134F),
    (0x31350, 0x323AF),
    (0x323B0, 0x3347F),
)


def count_hanzi(text: str) -> int:
    """返回文本中的汉字个数。"""
    return sum(
        any(start <= ord(ch) <= end for start, end in _HANZI_RANGES)
        for ch in text
    )


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    """返回出现次数最多的前 n 个英文单词及其次数。"""
    if n <= 0:
        return []

    words = (
        word.lower()
        for word in re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)*", text)
    )
    counts = Counter(words)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:n]
