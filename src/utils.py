# ../test/test_utils.py
import json
import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(funcName)s - %(levelname)s : %(message)s',
                    filename='../logs/utils.log',  # Запись логов в файл
                    filemode='w')
logger = logging.getLogger("app.utils")


def load_transactions(file_path: str) -> list:
    """принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Returned data from file {file_path}")
                return data
            else:
                logger.error(f'Incorrect input data in {file_path}')
                return []
        except json.JSONDecodeError:
            logger.error(f'Incorrect input data in {file_path}')
            return []
