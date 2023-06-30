import json
from datetime import datetime

filename = 'operations.json'


def load_data(filename):
    # Чтение данных из файла operations.json
    with open(filename, 'r', encoding='utf-8') as file:
        operations_data = json.load(file)
        return operations_data


def filter_sort(data):
    # вывод 5-ти последних операций
    items = [item for item in data if item.get('state') == "EXECUTED"]
    items.sort(key=lambda x: x.get('date'), reverse=True)
    return items[-5:]


def mask_card(str_):
    # маскирует номер карты и номер счета
    if str_ == None:
        return ''
    str_list = str_.split(' ')
    numb = str_list[-1]
    if len(str_list) > 2:
        return f'{str_list[0]} {str_list[1]} {numb[:4]} {numb[4:6]}** **** {numb[-4:]}'
    else:
        if str_list[0] == 'Счет':
            return f'{str_list[0]} ** {numb[-4:]}'
        return f'{str_list[0]} {numb[:4]} {numb[4:6]}** **** {numb[-4:]}'


def conv_date(data):
    """
    Форматирование даты
    """
    thedate = datetime.fromisoformat(data)
    date_formatted = thedate.strftime("%d.%m.%Y")
    return date_formatted


def prepare_data(sorted_data):
    # выводит результат сорnируя по заданию
    pripared_operations = []
    for data in sorted_data:
        date = data['date'].split('T')[0]
        description = data['description']
        masket_from_account = mask_card(data.get('from'))
        masket_to_account = mask_card(data.get('to'))
        amount = data['operationAmount']['amount']

        pripared_operation = {
            'date': date,
            'description': description,
            'from_account': masket_from_account,
            'to_account': masket_to_account,
            'amount': amount

        }
        pripared_operations.append(pripared_operation)
    return pripared_operations

