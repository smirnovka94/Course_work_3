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

def last_operation(json_list: list,count_operations=5) -> dict:
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