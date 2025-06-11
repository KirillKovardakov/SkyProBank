import re
from collections import Counter
from src.utils import load_transactions


def filter_by_state(list_dicts: list, state: str = 'EXECUTED') -> list:
    """Возвращает список, отфильтрованный по состоянию (state)"""
    if len(list_dicts) == 0 or not isinstance(state, str):
        raise ValueError
    filtered_by_state = []
    for transaction in list_dicts:
        if 'state' in transaction and isinstance(transaction.get("state"), str):
            if transaction.get('state').lower() == state.lower():
                filtered_by_state.append(transaction)
    return filtered_by_state


def sort_by_date(list_dicts: list, is_increase: bool = True) -> list:
    """Сортирует список по дате(date). По умолчанию - по убыванию"""
    if len(list_dicts) == 0 or not isinstance(is_increase, bool):
        raise ValueError
    sorted_list_by_date = sorted(list_dicts, key=lambda x: x.get('date'), reverse=is_increase)
    return sorted_list_by_date


def filter_by_state_re(transactions: list, state: str) -> list:
    """Возвращает список словарей, у которых в описании есть данная строка"""
    search_pattern = re.compile(re.escape(state), re.IGNORECASE)
    result = []
    for transaction in transactions:
        if 'description' in transaction and isinstance(transaction.get("description"), str):
            if search_pattern.search(transaction.get("description", "")):
                result.append(transaction)
    return result


def filter_by_description(transactions: list, categories: list) -> dict:
    """Возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""

    filtered_transactions = []
    for transaction in transactions:
        description = transaction.get('description', '')

        for category in categories:
            if re.search(category, description, re.IGNORECASE):
                filtered_transactions.append(description)
                break
    category_counter = Counter(filtered_transactions)
    return dict(category_counter)
