import pytest
import tempfile
import os
import json
from src.utils import load_transactions, read_excel_files
import pandas as pd
from unittest.mock import patch, mock_open


def test_file_not_exists():
    assert load_transactions("non_existing_file.json") == []


def test_valid_json_list():
    data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".json", encoding='utf-8') as tmp:
        json.dump(data, tmp)
        tmp_path = tmp.name
    try:
        assert load_transactions(tmp_path) == data
    finally:
        os.remove(tmp_path)


def test_json_not_a_list():
    data = {"id": 1, "amount": 100}
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".json", encoding='utf-8') as tmp:
        json.dump(data, tmp)
        tmp_path = tmp.name
    try:
        assert load_transactions(tmp_path) == []
    finally:
        os.remove(tmp_path)


def test_invalid_json():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".json", encoding='utf-8') as tmp:
        tmp.write("{ invalid json ]")
        tmp_path = tmp.name
    try:
        assert load_transactions(tmp_path) == []
    finally:
        os.remove(tmp_path)


def test_empty_file():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".json", encoding='utf-8') as tmp:
        tmp_path = tmp.name
    try:
        assert load_transactions(tmp_path) == []
    finally:
        os.remove(tmp_path)


def test_read_csv_file():
    mock_data = "col1,col2\n1,2\n3,4"
    with patch('builtins.open', mock_open(read_data=mock_data)), \
            patch('pandas.read_csv') as mock_read_csv, \
            patch('os.path.exists', return_value=True):
        mock_read_csv.return_value = pd.DataFrame({'col1': [1, 3], 'col2': [2, 4]})

        df = read_excel_files("../data/transactions.csv")

        mock_read_csv.assert_called_once_with("../data/transactions.csv", sep=None, engine='python')
        assert len(df) == 2


def test_read_xlsx_file():
    mock_data = pd.DataFrame({'col1': [1, 3], 'col2': [2, 4]})
    with patch('pandas.read_excel') as mock_read_excel, \
            patch('os.path.exists', return_value=True):  # Mock os.path.exists
        mock_read_excel.return_value = mock_data

        df = read_excel_files('../data/transactions_excel.xlsx')

        mock_read_excel.assert_called_once_with('../data/transactions_excel.xlsx')
        assert len(df) == 2


def test_file_not_found():
    with pytest.raises(FileNotFoundError, match="File not found!"):
        read_excel_files("non_existent_file.csv")
