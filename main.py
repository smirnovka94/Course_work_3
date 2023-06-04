from utils.functions import read_json, last_operation,  find_information, hidden_account

if __name__ == "__main__":
    file = 'operations.json'

    list_operations = read_json(file)
    index_date_operations = last_operation(list_operations)

    for key, value in index_date_operations.items():
        key = int(key)
        description = find_information(list_operations[key],'description') #Получаем тип операции

        sender_account = find_information(list_operations[key],'from') #Получаем счет отправителя
        sender_account = hidden_account(sender_account)
        recipient_account = find_information(list_operations[key],'to') #Получаем счет получателя
        recipient_account = hidden_account(recipient_account)

        cash = find_information(list_operations[key]['operationAmount'],'amount') #Получаем сумму перевода
        currency = find_information(list_operations[key]['operationAmount']['currency'],'name')  # Получаем валюту перевода

        #Собираем результат
        print(f"{value} {description}")
        if sender_account == "":
            print(recipient_account)
        else:
            print(f"{sender_account} -> {recipient_account}")
        print(f"{cash} {currency}\n")
