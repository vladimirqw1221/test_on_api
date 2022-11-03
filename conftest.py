import pytest

from random import randrange
from src.generators.player import Player


@pytest.fixture
def get_number():
    return randrange(1,1000,5)

@pytest.fixture
def get_player_generator():
    return Player()


def _calculite(a,b):
    if isinstance(a ,int) and isinstance(b , int):
        return a + b
    else:
        return None




@pytest.fixture
def calculite():
    return _calculite


@pytest.fixture
def make_number():
    # print(" I ' am getting number ")
    numner = randrange(1,1000,5)
    yield numner
    # print(f"print number in home {numner}")


