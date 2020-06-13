from functools import reduce
from typing import List, Callable


def markdown_headers(words: List[str], tag: str, convert: Callable[[str], str] = lambda w: w) -> List[str]:
    return [tag + ' ' + convert(word) for word in words]


def _md_row(row: List[str], convert: Callable[[str], str] = lambda w: w) -> str:
    return reduce((lambda accu, cur: accu + ' | ' + convert(cur)), row, '') + '|'


def markdown_table(header: List[str], table: List[List[str]]) -> List[str]:
    title = _md_row(header)
    delimiter = _md_row(header, lambda _: '---')
    body = [_md_row(row) for row in table[1:]]
    return [title, delimiter, *body]
