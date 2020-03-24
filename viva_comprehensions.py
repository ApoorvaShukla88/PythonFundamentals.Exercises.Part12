from itertools import chain
from typing import List, Dict, Set, Callable
import enum
import viva_comprehensions as vc


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param start:
    :param stop:
    :param parity:
    :return:
    """

    oddNum = []
    evenNum = []
    for i in range(start, stop):
        if i % 2 != 0:
            oddNum.append(i)
        elif i % 2 == 0:
            evenNum.append(i)

    if parity == vc.Parity.ODD:
        return oddNum
    elif parity == vc.Parity.EVEN:
        return evenNum


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    new_dict = dict()

    for i in range(start, stop):
        new_dict[i] = strategy(i)

    return new_dict


def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in:
    :return:
    """
    s = set()
    for i in list(val_in):
        if i.islower():
            s.add(i.upper())

    return s
