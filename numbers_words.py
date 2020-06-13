import argparse
from pathlib import Path
from subprocess import Popen

from src.format import markdown
from src.num_to_words import num_to_words


def write_markdown(boundary: int, path: str = './out') -> Path:
    words = [(str(num) + ': ' + num_to_words(num)) for num in range(0, boundary)]
    md = markdown(words, '######')
    print(md)

    output = Path(path, 'numbers').with_suffix('.md')
    with open(output, 'w') as f:
        for line in md:
            f.write(line + '\n')
    return output


dict_para = 'name'
parser = argparse.ArgumentParser()
parser.add_argument(dict_para)
args = vars(parser.parse_args())


high = int(args[dict_para]);
md_file = write_markdown(high)
Popen(['typora', md_file], close_fds=True)
