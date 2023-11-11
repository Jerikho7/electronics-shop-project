"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture()
def item_for_test():
    return Item("Television", 150000, 5)


@pytest.fixture()
def item_for_test2():
    return Item("Refrigerator", 50000, 10)


@pytest.fixture()
def phone_for_test():
    return Phone("iPhone 15 Pro Max", 120000, 5, 1)


def test_calculate_total_price(item_for_test):
    assert item_for_test.calculate_total_price() == 750000


def test_apply_discount(item_for_test):
    assert item_for_test.apply_discount() == 150000


def test_name(item_for_test, item_for_test2):
    item_for_test2.name = "Refrigerator"
    assert repr(item_for_test2) == "Item('Refrigerat', 50000, 10)"
    item_for_test.name = "Television"
    assert repr(item_for_test) == "Item('Television', 150000, 5)"


def test_instantiate_from_csv():
    Item.instantiate_from_csv("../src/items.csv")
    item1 = Item.all[0]
    assert item1.price == '100'
    assert item1.quantity == '1'


def test_string_to_number():
    assert Item.string_to_number('100') == 100
    assert Item.string_to_number('150000.0') == 150000
    assert Item.string_to_number('250.50') == 250


def test_str(item_for_test):
    assert str(item_for_test) == "Television"


def test_repr(item_for_test):
    assert repr(item_for_test) == "Item('Television', 150000, 5)"


def test_add(item_for_test, phone_for_test):
    assert item_for_test.quantity + phone_for_test.quantity == 10
