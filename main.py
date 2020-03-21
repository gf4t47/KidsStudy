from pathlib import Path

from data.word_dictionary import dictionary
from src.randomization import shuffle_list
from src.format import markdown
import argparse


def write_markdown(name: str, path: str = './out') -> None:
    s = shuffle_list(dictionary[name])
    md = markdown(s)
    print(md)

    with open(Path(path, name).with_suffix('.md'), 'w') as f:
        for line in md:
            f.write(line + '\n')


dict_para = 'name'
parser = argparse.ArgumentParser()
parser.add_argument(dict_para)
args = vars(parser.parse_args())
write_markdown(args[dict_para])
