import pytest
from HW5 import people, shelf, add, delete_document

FIXTURES_1 = [
    ("2207 876234", "Василий Гупкин"),
    ("11-2", "Геннадий Покемонов"),
    ("10006", "Аристарх Павлов"),
    ("1234", None)
]

FIXTURES_2 = [
    ("2207 876234", 1),
    ("11-2""", 1),
    ("5455 028765", 1),
    ("10006", 2),
    ("1234", "Такого документа нет")
]

FIXTURES_3 = [
    ("Pasport", "12345", "Egor", 2, "Данные добавлены"),
    ("ID", "112233", "Oleg", 1, "Данные добавлены"),
    ("License", "ff1384", "God Blessed", 4, "Такой полки нет"),
]


@pytest.mark.parametrize("user_num, test_result", FIXTURES_1)
def test_people(user_num, test_result):
    result = people(user_num)
    assert test_result == result


@pytest.mark.parametrize("doc_num, test_result", FIXTURES_2)
def test_shelf(doc_num, test_result):
    assert test_result == shelf(doc_num)


@pytest.mark.parametrize("type_, number, name, shelf_num, test_result", FIXTURES_3)
def test_add(type_, number, name, shelf_num, test_result):
    assert test_result == add(type_, number, name, shelf_num)


def test_delete_document():
    result = 'Документ 11-2 удален'
    assert delete_document("11-2") == result
