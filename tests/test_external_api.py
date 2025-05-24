import pytest
from unittest.mock import patch
from src.external_api import convert_to_rub


@patch('src.external_api.os.getenv')
@patch('src.external_api.requests.get')
def test_convert_rub_currency(mock_get, mock_getenv):
    mock_getenv.return_value = 'fake_api_key'
    transaction = {'amount': 100, 'currency': 'RUB'}
    result = convert_to_rub(transaction)
    assert result == 100.0
    mock_get.assert_not_called()


@patch('src.external_api.os.getenv')
@patch('src.external_api.requests.get')
def test_convert_usd_to_rub_success(mock_get, mock_getenv):
    mock_getenv.return_value = 'fake_api_key'
    transaction = {'amount': 10, 'currency': 'USD'}

    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'rates': {'RUB': 90.0}
    }

    result = convert_to_rub(transaction)
    assert result == 900.0


@patch('src.external_api.os.getenv')
@patch('src.external_api.requests.get')
def test_convert_currency_not_found(mock_get, mock_getenv):
    mock_getenv.return_value = 'fake_api_key'
    transaction = {'amount': 10, 'currency': 'EUR'}

    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'rates': {}
    }

    result = convert_to_rub(transaction)
    assert result == 10.0


@patch('src.external_api.os.getenv')
@patch('src.external_api.requests.get')
def test_api_failure(mock_get, mock_getenv):
    mock_getenv.return_value = 'fake_api_key'
    transaction = {'amount': 50, 'currency': 'GBP'}

    mock_response = mock_get.return_value
    mock_response.status_code = 500

    result = convert_to_rub(transaction)
    assert result == 50.0
