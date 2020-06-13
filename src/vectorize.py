from random import shuffle
from typing import Iterable, Sequence, List


def shuffle_list(items: List[str]) -> List[str]:
    """
    copy and shuffle
    :param items: input word dictionary
    :return: shuffled list
    """
    ret = items.copy()
    shuffle(ret)
    return ret
