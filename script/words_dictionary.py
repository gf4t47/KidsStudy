from pathlib import Path

from data.word_dictionary import dictionary
from src.vectorize import shuffle_list
from src.format import markdown_headers
from subprocess import Popen
import argparse


def write_markdown(name: str, path: str = './out') -> Path:
    """
    :param name: key in dictionary
    :param path: output path
    :return: output file IO ref
    """
    key = name.lower()
    if key not in dictionary:
        raise KeyError(f'Unknown words dictionary {name}')

    s = shuffle_list(dictionary[key])
    md = markdown_headers(s, '#', lambda w: w.capitalize())
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

md_file = write_markdown(args[dict_para])
Popen(['typora', md_file], close_fds=True)
