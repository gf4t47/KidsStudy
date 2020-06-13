import argparse
from pathlib import Path
from subprocess import Popen
from typing import Tuple

from src.format import markdown_table
from src.num_to_words import num_to_words


def write_markdown(pair: Tuple[int, int], path: str = './out') -> Path:
    """
    :param pair: range
    :param path: output path
    :return: output file IO ref
    """
    (low_boundary, high_boundary) = pair
    num_word_pairs = [(str(num), num_to_words(num)) for num in range(low_boundary, high_boundary)]
    md = markdown_table(('Number', 'Words'), num_word_pairs)
    print(md)

    output = Path(path, f'{low_boundary}_{high_boundary}').with_suffix('.md')
    with open(output, 'w') as f:
        for line in md:
            f.write(line + '\n')
    return output


para_name = 'range'
parser = argparse.ArgumentParser()
parser.add_argument(para_name, type=int, nargs='+')
args = vars(parser.parse_args())[para_name]
[low, high] = [args[0], args[1]] if len(args) > 1 else [0, args[0]]


md_file = write_markdown((low, high))
Popen(['typora', md_file], close_fds=True)
