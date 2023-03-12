"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def example():
    return Item("Смартфон", 10000, 20)


def test_item_init(example):
    assert example.name == "Смартфон"
    assert example.price == 10000
    assert example.quantity == 20


def test_item_calculate_total_price(example):
    assert example.calculate_total_price() == 200000


def test_item_apply_discount(example):
    Item.pay_rate = 0.8
    example.apply_discount()
    assert example.price == 8000.0
