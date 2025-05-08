from typing import Union


def filter_by_state(list_dicts: list, state: str = 'EXECUTED') -> list:
    """Возвращает список, отфильтрованный по состоянию (state)"""
    filtered_by_state = [dictionary for dictionary in list_dicts if dictionary.get('state') == state]
    return filtered_by_state


def sort_by_date(list_dicts: list, reversed: bool = True) -> list:
    """Сортирует список по дате(date)"""
    sorted_list_by_date = sorted(list_dicts, key=lambda x: x.get('date'), reverse=reversed)
    return sorted_list_by_date
