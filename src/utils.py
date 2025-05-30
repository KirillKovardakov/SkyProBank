# ../test/test_utils.py
import json
import os


def load_transactions(file_path: str) -> list:
    """принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
        except json.JSONDecodeError:
            return []
