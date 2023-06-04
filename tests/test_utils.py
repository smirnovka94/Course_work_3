import os.path
import pytest

from utils.functions import read_json, rewrite_date, last_operation, export_full_inf

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

@pytest.fixture
def expexted_result_export_full_inf():
    return ["30.06.2019 Перевод с карты на карту", '19.04.2019 Перевод со счета на счет"]
def test_export_full_inf(expexted_test_last_operation, expexted_result_export_full_inf):
    """Тест на вывод основной информации по индексу"""
    test_json = read_json(filename)
    assert export_full_inf(test_json, expexted_test_last_operation) == expexted_result_export_full_inf

