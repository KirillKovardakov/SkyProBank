import pytest
from unittest.mock import patch
from src.main import main


def test_main_json_filter_executed_rub(monkeypatch, capsys, fake_transactions):
    # Подмена ввода пользователя
    inputs = iter([
        '1',  # JSON-файл
        'EXECUTED',  # Статус
        'да',  # Сортировка
        'по убыванию',  # Тип сортировки
        'да',  # Только рубли
        'да',  # Фильтр по слову
        'организации'  # Ключевое слово
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Подмена загрузки файла
    with patch('src.main.load_transactions', return_value=fake_transactions), \
            patch('src.main.read_excel_files', return_value=[]):
        main()

    out, err = capsys.readouterr()
    assert "Для обработки выбран JSON-файл." in out
    assert 'Операции отфильтрованы по статусу "EXECUTED"' in out
    assert "Распечатываю итоговый список транзакций..." in out
    assert "Всего банковских операций в выборке: 1" in out
    assert "01.01.2022 Перевод организации" in out
    assert "Сумма: 1000.00 руб." in out


def test_main_invalid_file_format_raises(monkeypatch):
    inputs = iter([
        '4'  # Неверный формат → должен вызвать ValueError
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with patch('src.main.load_transactions', return_value=[]), \
            patch('src.main.read_excel_files', return_value=[]):
        with pytest.raises(ValueError):
            main()


def test_main_sort_ascending(monkeypatch, capsys):
    fake_data = [
        {"id": 1, "state": "EXECUTED", "date": "2022-01-02T10:00:00", "description": "Test",
         "operationAmount": {"amount": "100", "currency": {"name": "руб.", "code": "RUB"}}, "to": "Счет 123"},
        {"id": 2, "state": "EXECUTED", "date": "2022-01-01T10:00:00", "description": "Test",
         "operationAmount": {"amount": "200", "currency": {"name": "руб.", "code": "RUB"}}, "to": "Счет 456"}
    ]
    inputs = iter([
        '1', 'executed',
        'да', 'по возрастанию',
        'нет', 'нет'
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with patch('src.main.load_transactions', return_value=fake_data):
        main()

    out, _ = capsys.readouterr()
    # дата отсортирована по возрастанию — "2022-01-01" должна быть первой
    assert "01.01.2022" in out


def test_main_print_to_only(monkeypatch, capsys):
    fake_data = [
        {"id": 1, "state": "EXECUTED", "date": "2022-01-01T10:00:00", "description": "Test",
         "operationAmount": {"amount": "123", "currency": {"name": "руб.", "code": "RUB"}},
         "to": "Счет 12345678901234567890"}
    ]
    inputs = iter(['1', 'executed', 'нет', 'нет', 'нет'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with patch('src.main.load_transactions', return_value=fake_data):
        main()

    out, _ = capsys.readouterr()
    assert "Счет **7890" in out


def test_main_print_amount_with_currency_name(monkeypatch, capsys):
    fake_data = [
        {"id": 1, "state": "EXECUTED", "date": "2022-01-01T10:00:00", "description": "Test",
         "currency_name": "руб.", "amount": "555", "to": "Счет 12345678901234567890"}
    ]
    inputs = iter(['1', 'executed', 'нет', 'нет', 'нет'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with patch('src.main.load_transactions', return_value=fake_data):
        main()

    out, _ = capsys.readouterr()
    assert "Сумма: 555 руб." in out
