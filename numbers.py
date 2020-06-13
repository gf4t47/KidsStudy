import argparse
from pathlib import Path
from subprocess import Popen

from src.format import markdown
from src.to_words import num_words


def write_markdown(boundary: int, path: str = './out') -> Path:
    words = [num_words(num) for num in range(1, boundary)]
    md = markdown(words, '##')
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

md_file = write_markdown(args[dict_para])
Popen(['typora', md_file], close_fds=True)
