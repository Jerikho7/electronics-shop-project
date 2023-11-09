"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

item_for_test = Item("Television", 150000, 5)
item_for_test2 = Item("Refrigerator", 50000, 10)


def test_calculate_total_price():
    assert item_for_test.calculate_total_price() == 750000


def test_apply_discount():
    assert item_for_test.apply_discount() == 150000


def test_name():
    item_for_test2.name = "Refrigerator"
    assert item_for_test2.__repr__() == "Item('Refrigerat', 50000, 10)"


def test_instantiate_from_csv():
    Item.instantiate_from_csv("../src/items.csv")
    item1 = Item.all[0]
    assert item1.price == '100'
    assert item1.quantity == '1'


def test_string_to_number():
    assert Item.string_to_number('100') == 100
    assert Item.string_to_number('150000.0') == 150000
    assert Item.string_to_number('250.50') == 250


def test_str():
    assert str(item_for_test) == "Television"


def test_repr():
    assert repr(item_for_test) == "Item('Television', 150000.0, 5)" #не могу понять почему float а не int
