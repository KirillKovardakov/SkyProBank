# ../test/test_external_api.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction: dict) -> float:
    """принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""
    api_key = os.getenv('API_KEY')
    amount = transaction['amount']
    currency = transaction['currency']

    if currency == "RUB":
        return float(amount)

    response = requests.get(f'https://api.apilayer.com/exchangerates_data/latest?base={currency}&apikey={api_key}')

    if response.status_code == 200:
        rates = response.json().get('rates', {})
        rub_rate = rates.get('RUB')
        if rub_rate:
            return float(amount) * rub_rate
    return float(amount)  # если валюта не найдена, возвращаем исходную сумму
