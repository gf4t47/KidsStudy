from typing import List


def markdown(words: List[str], tag: str = '#') -> List[str]:
    return [tag + ' ' + word.capitalize() for word in words]
