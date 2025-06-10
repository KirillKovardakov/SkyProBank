def filter_by_currency(transactions: list[dict], currency_code: str) -> iter:
    """Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""

    if (not isinstance(currency_code, str) or not isinstance(transactions, list)
            or len(transactions) == 0):
        raise ValueError

    for transaction in transactions:
        if "operationAmount" in transaction and "currency" in transaction["operationAmount"] and "code" in \
                transaction["operationAmount"][
                    "currency"]:
            if transaction.get('operationAmount').get('currency').get('code') == currency_code:
                yield transaction
        elif 'currency_code' in transaction:
            if transaction.get('currency_code') == currency_code:
                yield transaction


def transaction_descriptions(transactions: list[dict]) -> iter:
    """Возвращает описание каждой операции транзакции по очереди"""

    if not isinstance(transactions, list) or len(transactions) == 0:
        raise ValueError
    for transaction in transactions:
        yield transaction['description']


def card_number_generator(start: int, end: int) -> iter:
    for number in range(start, end + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[
                                                                         8:12] + " " + f"{number:016d}"[12:]
