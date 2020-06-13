from functools import reduce
from typing import Callable, Iterable


def markdown_headers(words: Iterable[str], tag: str, convert: Callable[[str], str] = lambda w: w) -> Iterable[str]:
    return [tag + ' ' + convert(word) for word in words]


def _md_row(row: Iterable[str], convert: Callable[[str], str] = lambda w: w) -> str:
    return reduce((lambda accu, cur: accu + ' | ' + convert(cur)), row, '') + '|'


def markdown_table(header: Iterable[str], table: Iterable[Iterable[str]]) -> Iterable[str]:
    title = _md_row(header)
    delimiter = _md_row(header, lambda _: '---')
    body = [_md_row(row) for row in table[1:]]
    return [title, delimiter, *body]
