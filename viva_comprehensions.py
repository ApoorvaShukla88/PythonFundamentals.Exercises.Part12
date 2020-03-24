from itertools import chain
from typing import List, Dict, Set, Callable
import enum
import viva_comprehensions as vc


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
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
    new_dict = dict()

    for i in range(start, stop):
        new_dict[i] = strategy(i)

    return new_dict


def gen_set(val_in: str) -> Set:
    s = set()
    for i in list(val_in):
        if i.islower():
            s.add(i.upper())

    return s
