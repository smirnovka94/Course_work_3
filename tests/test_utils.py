import os.path
import pytest

from utils.functions import read_json, rewrite_date, last_operation

filename = os.path.join(os.path.dirname(__file__), 'test.json')
def test_read_json(expexted_result_for_read_json):
    """Пест на чтение JSON"""
    assert read_json(filename) == expexted_result_for_read_json

def test_rewrite_date():
    """Тест на обработку даты"""
    assert rewrite_date("2002-12-25") == "25.12.2002"

def test_last_operation():
    """Тест на вывод последних операций"""
    test_json = read_json(filename)
    assert last_operation(test_json, 2) == {'0': '30.06.2019', '1': '19.04.2019'}
