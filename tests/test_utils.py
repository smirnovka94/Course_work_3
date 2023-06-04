import os.path
import pytest

from utils.functions import read_json, rewrite_date, last_operation, export_full_inf, hidden_account, find_information

filename = os.path.join(os.path.dirname(__file__), 'test.json')
def test_read_json(expexted_result_for_read_json):
    """Пест на чтение JSON"""
    assert read_json(filename) == expexted_result_for_read_json

def test_rewrite_date():
    """Тест на обработку даты"""
    assert rewrite_date("2002-12-25") == "25.12.2002"

def test_last_operation(expexted_test_last_operation):
    """Тест на вывод последних операций и индекса"""
    test_json = read_json(filename)
    assert last_operation(test_json, 2) == expexted_test_last_operation


def test_hidden_account():
    """Тест на скрытие номера счета"""
    assert hidden_account("Visa Platinum 1813166339376336") == "Visa Platinum 1813 16** **** 6336"
    assert hidden_account("Счет 97848259954268659635") == "Счет **9635"

def test_find_information(dictionies1, dictionies2):
    """Тест на наличие значений"""
    assert find_information(dictionies1,"from") == ''
    assert find_information(dictionies2, "from") == 'Maestro 1913883747791351'


