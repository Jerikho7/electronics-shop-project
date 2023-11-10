import pytest
from src.phone import Phone


@pytest.fixture()
def phone_for_test():
    return Phone("iPhone", 120000, 5, 1)


@pytest.fixture()
def phone_for_test2():
    return Phone("Samsung", 90000, 10, 2)


def test_str(phone_for_test2):
    assert str(phone_for_test2) == "Samsung"


def test_repr(phone_for_test):
    assert repr(phone_for_test) == "Phone('iPhone', 120000, 5, 1)"


def test_number_sim(phone_for_test):
    phone_for_test.number_sim = 1
    assert repr(phone_for_test) == "Phone('iPhone', 120000, 5, 1)"
    phone_for_test.number_sim = 0
    assert repr(phone_for_test) == ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
