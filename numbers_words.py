import argparse
from pathlib import Path
from subprocess import Popen

from src.format import markdown_table
from src.num_to_words import num_to_words


def write_markdown(high: int, low: int, path: str = './out') -> Path:
    words = [[str(num), num_to_words(num)] for num in range(low, high)]
    md = markdown_table(['Number', 'Words'], words)
    print(md)

    output = Path(path, 'numbers').with_suffix('.md')
    with open(output, 'w') as f:
        for line in md:
            f.write(line + '\n')
    return output


para_name = 'range'
parser = argparse.ArgumentParser()
parser.add_argument(para_name, type=int, nargs='+')
args = vars(parser.parse_args())[para_name]
[low, high] = [args[0], args[1]] if len(args) > 1 else [0, args[0]]


md_file = write_markdown(high, low)
Popen(['typora', md_file], close_fds=True)
