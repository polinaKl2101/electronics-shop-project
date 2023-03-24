import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def example():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1


def test_item_init(example):
    assert example.getname == "iPhone 14"
    assert example.price == 120_000
    assert example.quantity == 5
    assert example.number_of_sim == 2


def test_str(example):
    assert str(example) == 'iPhone 14'


def test_repr(example):
    assert repr(example) == "Phone('iPhone 14', 120000, 5, 2)"

