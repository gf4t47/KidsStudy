from typing import List


def markdown(words: List[str], tag: str = '#') -> List[str]:
    return [tag + ' ' + word + '/r/n' for word in words]
