import json
import operator
import datetime

def read_json(filename)-> list:
    """
    :move: Чтение json
    :return: Список словарей
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data_json = json.load(file)
    return data_json

def rewrite_date(date: str) -> str:
    """
    Преобразует исходный формат даты YYYY-MM-DD в DD.MM.YYYY
    :param date:
    :return: right_date:
    """
    new_date = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%d.%m.%Y')
    return new_date

def find_information(dictionaries: dict, key: str)->str:
    """
    Проверяет в списке из словарей наличие значений. В противном случае возвращает  пустой текст
    :param dictionaries:
    :param key:
    :return:
    """
    try:
        return dictionaries[key]
    except KeyError:
        return ""
def last_operation(json_list: list, count_operations=5) -> dict:
    """
     1.Получает список словарей из JSON файла
     2 обрабатывает каждый словарь на наличие статуса "EXECUTED"
     3.Отбирает словари по ключю <date>
     4.Сортирует весь список <date> и возвращачет индекс и дату последних операций (по умолчанию 5)
    :param json_list, count_operations:
    :return:dict_index_date
    """
    dict_date_full = {}
    dict_date = {}
    i = 0
    for dictionaries in json_list:
        #фильтр по пустому словарю
        try:
            state = dictionaries['state']
        except KeyError:
            i += 1
            continue
        # ищем "EXECUTED"
        if state == "EXECUTED":
            # Ищем дату операции
            date = dictionaries['date']
            # Делаем словарь- где Ключ: индекс JSON списка, а Значение: дата
            dict_date_full[str(i)] = date
            date_split = date.split('T')
            # Делаем словарь- где Ключ: индекс JSON списка, а Значение: преобразованная по формату дата
            right_date = rewrite_date(date_split[0])
            dict_date[str(i)] = right_date
            i += 1
    # Сортируем словарь
    sort_data = sorted(dict_date_full.items(), key=operator.itemgetter(1), reverse=True)
    i = 0
    dict_index_date = {}

    while i != count_operations:
        index_date = sort_data[i][0]
        dict_index_date[index_date] = dict_date[index_date]
        i += 1
    return dict_index_date

def hidden_account(account: str) -> str:
    """
    Преобразует номер счета в скрытый с ***
    :param account:
    :return:
    """
    text_split = account.split(' ')
    right_account = " ".join(text_split[:-1])
    number_account = text_split[-1]
    len_number = len(number_account)
    if len_number == 16:
        for i, item in enumerate(number_account):
            if (i) % 4 == 0:
                right_account = right_account + " "
            if 5 < i < 12:
                right_account = right_account + "*"
            else:
                right_account = right_account + item
    else:
        right_account = f"{right_account} **{number_account[-4:]}"
    return right_account

def export_full_inf(index_date, data_dict):

    for key, value in index_date.items():
        key = int(key)
        description = data_dict[key]['description']  # Получаем тип операции
        sender_account = data_dict[key]['from']  # Получаем счет отправителя
        sender_account = hidden_account(sender_account)
        recipient_account = data_dict[key]['to']  # Получаем счет получателя
        recipient_account = hidden_account(recipient_account)

        cash = data_dict[key]['operationAmount']['amount']  # Получаем сумму перевода
        currency = data_dict[key]['operationAmount']['currency']['name']  # Получаем валюту перевода

        print(f"{value} {description}")
        print(f"{sender_account} -> {recipient_account}")
        print(f"{cash} {currency}\n")
