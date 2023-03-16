"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def example():
    item = Item("Смартфон", 10000, 20)
    return item


def test_item_init(example):
    assert example.getname == "Смартфон"
    assert example.price == 10000
    assert example.quantity == 20


def test_item_calculate_total_price(example):
    assert example.calculate_total_price() == 200000


def test_item_apply_discount(example):
    Item.pay_rate = 0.8
    example.apply_discount()
    assert example.price == 8000.0


def test_getname(example):
    assert example.getname == 'Смартфон'


def test_instantiate_from_csv():
    Item.instantiate_from_csv(csv_file='../src/items.csv')


def test_string_to_number():
    assert Item.string_to_number('5.5') == 5
