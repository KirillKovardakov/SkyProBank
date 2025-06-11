from src.utils import load_transactions, read_excel_files
from src.processing import filter_by_state_re, sort_by_date, filter_by_state
from src.generators import filter_by_currency
from src.widget import get_date, mask_account_card


def main():
    ALLOWED_LIST_OF_STATUSES = ['executed', 'canceled', 'pending']
    CONSOLE_GET_STATUS = f"Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
    filepath = ''
    import_transactions = []
    user_file_format = input("""
    Привет! Добро пожаловать в программу работы 
    с банковскими транзакциями. 
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла\n""")

    if user_file_format == '1':
        print("Для обработки выбран JSON-файл.")
        import_transactions = load_transactions('../data/operations.json')
    elif user_file_format == '2':
        print("Для обработки выбран CSV-файл.")
        import_transactions = read_excel_files('../data/transactions.csv')
    elif user_file_format == '3':
        print("Для обработки выбран XLSX-файл.")
        import_transactions = read_excel_files('../data/transactions_excel.xlsx')
    else:
        raise ValueError

    user_status = input(CONSOLE_GET_STATUS)
    while user_status.lower() not in ALLOWED_LIST_OF_STATUSES:
        user_status = input(CONSOLE_GET_STATUS)

    print(f'Операции отфильтрованы по статусу "{user_status}"')

    transactions = (filter_by_state(import_transactions, user_status))
    user_console = input("Отсортировать операции по дате? Да/Нет\n")
    if user_console.lower() == 'да':
        user_console = input("Отсортировать по возрастанию или по убыванию?\n")
        if user_console == 'по убыванию':
            transactions = sort_by_date(transactions)
        elif user_console == 'по возрастанию':
            transactions = sort_by_date(transactions, False)
    user_console = input('Выводить только рублевые транзакции? Да/Нет\n')
    if user_console.lower() == 'да':
        transactions = [transaction_iter for transaction_iter in filter_by_currency(transactions, 'RUB')]
    user_console = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n')
    if user_console.lower() == 'да':
        user_key_description = input('Введите ключевое слово для поиска:\n')
        transactions = filter_by_state_re(transactions, user_key_description)
    print('Распечатываю итоговый список транзакций...')
    if len(transactions) == 0:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
    else:
        print(f'Всего банковских операций в выборке: {len(transactions)}')
        for transaction in transactions:
            print(f"{get_date(transaction.get('date'))} {transaction.get('description')}")
            if 'from' in transaction and 'to' in transaction and transaction.get('from'):
                print(f'{mask_account_card(transaction.get("from"))} -> {mask_account_card(transaction.get("to"))}')
            elif 'to' in transaction:
                print(f'{mask_account_card(transaction.get("to"))}')
            if "operationAmount" in transaction and (
                    "currency" in transaction["operationAmount"] and "amount" in transaction["operationAmount"]) and (
                    "name" in transaction["operationAmount"]["currency"]):
                print(
                    f"Сумма: {transaction.get('operationAmount').get('amount')} {transaction.get('operationAmount').get('currency').get('name')}")
            elif 'currency_name' in transaction and 'amount' in transaction:
                print(f"Сумма: {transaction.get('amount')} {transaction.get('currency_name')}")
            print()


if __name__ == '__main__':
    main()
