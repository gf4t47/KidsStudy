from typing import List, Callable


def markdown(words: List[str], tag: str = '#', convert: Callable[[str], str] = lambda w: w) -> List[str]:
    return [tag + ' ' + convert(word) for word in words]
