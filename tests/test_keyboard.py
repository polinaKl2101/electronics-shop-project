import pytest
from src.item import Item
from src.keyboard import KeyBoard


@pytest.fixture
def example():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    return kb


def test_item_init(example):
    assert example.getname == "Dark Project KD87A"
    assert example.price == 9600
    assert example.quantity == 5


def test_change_lang(example):
    assert str(example.language) == "EN"
    example.change_lang()
    assert str(example.language) == "RU"
    example.change_lang().change_lang().change_lang()
    assert str(example.language) == "EN"



