from pathlib import Path

from data.word_dictionary import dictionary
from src.randomization import shuffle_list
from src.format import markdown
from subprocess import Popen
import argparse


def write_markdown(name: str, path: str = './out') -> Path:
    s = shuffle_list(dictionary[name])
    md = markdown(s)
    print(md)

    output = Path(path, name).with_suffix('.md')
    with open(output, 'w') as f:
        for line in md:
            f.write(line + '\n')
    return output


dict_para = 'name'
parser = argparse.ArgumentParser()
parser.add_argument(dict_para)
args = vars(parser.parse_args())
md_file = write_markdown(args[dict_para].lower())
Popen(['typora', md_file], close_fds=True)
