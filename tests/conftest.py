import pytest


@pytest.fixture
def expexted_result_for_read_json():
    return [
        {
            "id": 414894334,
            "state": "EXECUTED",
            "date": "2019-06-30T15:11:53.136004",
            "operationAmount": {
                "amount": "95860.47",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 59956820797131895975",
            "to": "Счет 43475624104328495820"
        },
        {},
        {
            "id": 509552992,
            "state": "EXECUTED",
            "date": "2019-04-19T12:02:30.129240",
            "operationAmount": {
                "amount": "81513.74",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Maestro 9171987821259925",
            "to": "МИР 2052809263194182"
        },
        {
            "id": 596914981,
            "state": "EXECUTED",
            "date": "2018-04-16T17:34:19.241289",
            "operationAmount": {
                "amount": "65169.27",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1813166339376336",
            "to": "Счет 97848259954268659635"
        },
        {
            "id": 200634844,
            "state": "CANCELED",
            "date": "2018-02-13T04:43:11.374324",
            "operationAmount": {
                "amount": "42210.20",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 33355011456314142963",
            "to": "Счет 45735917297559088682"
        },
        {
            "id": 879660146,
            "state": "EXECUTED",
            "date": "2018-07-22T07:42:32.953324",
            "operationAmount": {
                "amount": "92130.50",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 19628854383215954147",
            "to": "Счет 90887717138446397473"
        },
        {
            "id": 893507143,
            "state": "EXECUTED",
            "date": "2018-02-03T07:16:28.366141",
            "operationAmount": {
                "amount": "90297.21",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 37653295304860108767"
        },
        {
            "id": 710136990,
            "state": "CANCELED",
            "date": "2018-08-17T03:57:28.607101",
            "operationAmount": {
                "amount": "66906.45",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1913883747791351",
            "to": "Счет 11492155674319392427"
        }
    ]