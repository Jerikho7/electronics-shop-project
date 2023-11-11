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
    assert repr(phone_for_test) == "Phone('iPhone', 120000, 5, 1)"


def test_match(phone_for_test):
    with pytest.raises(ValueError, match=r"Количество физических SIM-карт должно быть целым числом больше нуля"):
        phone_for_test.number_sim = 0
        test_number_sim(phone_for_test)
