# ../test/test_utils.py
import json
import os
import logging
import pandas as pd
import csv
from pathlib import Path

from black.linegen import delimiter_split
from pandas.core.interchange.dataframe_protocol import DataFrame

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(funcName)s - %(levelname)s : %(message)s',
                    filename='../logs/utils.log',  # Запись логов в файл
                    filemode='w')
logger = logging.getLogger("app.utils")


def load_transactions(file_path: str) -> list:
    """принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    if not os.path.exists(file_path):
        logger.error(f'File not found {file_path}')
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


def read_excel_files(filepath: str) -> DataFrame:
    if not os.path.exists(filepath):
        logger.error(f'File not found {filepath}')
        raise FileNotFoundError("File not found!")
    try:
        if Path(filepath).suffix == ".csv":
            logging.info(f'Reading csv file {filepath}')
            df = pd.read_csv(filepath, sep=None, engine='python')
        elif Path(filepath).suffix == ".xlsx":
            logging.info(f'Reading xlsx file {filepath}')
            df = pd.read_excel(filepath)
        return df

    except Exception:
        logger.error(f'Something went wrong in {filepath}')
        raise Exception('Something went wrong')
