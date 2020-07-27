import math
import re
from collections import namedtuple
from typing import List

Audio = namedtuple('Audio', 'artist title')


def clear_string(text: str) -> str:
    # "feat." => ", "
    text = re.sub(r'feat\.?', ', ', text)

    # remove all text in brackets
    text = re.sub(r'\((.*?)\)', '', text)
    text = re.sub(r'\[(.*?)\]', '', text)

    text = re.sub(r'[^А-яA-z0-9,.() ]', ' ', text)
    return re.sub(r' +', ' ', text).strip()


def chunk(array: List, batch_size: int = 100):
    offset = 0
    for i in range(math.floor(len(array) // batch_size)):
        yield array[offset: offset + batch_size]
        offset += batch_size
