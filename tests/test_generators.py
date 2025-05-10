import src.generators as generators
import pytest


def test_filter_by_currency(list_of_transactions_fixture):
    assert_function = generators.filter_by_currency(list_of_transactions_fixture, 'USD')
    assert next(assert_function) == {'id': 939719570,
                                     'state': 'EXECUTED',
                                     'date': '2018-06-30T02:08:58.425572',
                                     'operationAmount': {
                                         'amount': '9824.07',
                                         'currency': {'name': 'USD',
                                                      'code': 'USD'}},
                                     'description': 'Перевод организации',
                                     'from': 'Счет 75106830613657916952',
                                     'to': 'Счет 11776614605963066702'}
    assert next(assert_function) == {'id': 142264268,
                                     'state': 'EXECUTED',
                                     'date': '2019-04-04T23:20:05.206878',
                                     'operationAmount': {
                                         'amount': '79114.93',
                                         'currency': {'name': 'USD',
                                                      'code': 'USD'}},
                                     'description': 'Перевод со счета на счет',
                                     'from': 'Счет 19708645243227258542',
                                     'to': 'Счет 75651667383060284188'}
    assert_function = generators.filter_by_currency(list_of_transactions_fixture, 'RUB')
    assert next(assert_function) == {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',
                                     'operationAmount': {'amount': '43318.34',
                                                         'currency': {'name': 'руб.', 'code': 'RUB'}},
                                     'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719',
                                     'to': 'Счет 74489636417521191160'}
    assert next(assert_function) == {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689',
                                     'operationAmount': {'amount': '67314.70',
                                                         'currency': {'name': 'руб.', 'code': 'RUB'}},
                                     'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588',
                                     'to': 'Счет 14211924144426031657'}


def test_filter_by_currency_invalid(list_of_transactions_fixture):
    with pytest.raises(ValueError):
        next(generators.filter_by_currency(list_of_transactions_fixture, 'EURO'))
    with pytest.raises(ValueError):
        next(generators.filter_by_currency('list_of_transactions_fixture', 'RUB'))
    with pytest.raises(ValueError):
        next(generators.filter_by_currency(list_of_transactions_fixture, 124))
    with pytest.raises(ValueError):
        next(generators.filter_by_currency([], 'RUB'))
    with pytest.raises(ValueError):
        next(generators.filter_by_currency([], 'EURO'))


def test_transaction_descriptions(list_of_transactions_fixture):
    expected = ['Перевод организации',
                'Перевод со счета на счет',
                'Перевод со счета на счет',
                'Перевод с карты на карту',
                'Перевод организации']
    descriptions = generators.transaction_descriptions(list_of_transactions_fixture)
    assert list([next(descriptions) for _ in range(5)]) == expected


def test_transaction_descriptions_invalid(list_of_transactions_fixture):
    with pytest.raises(ValueError):
        next(generators.transaction_descriptions([]))


def test_card_number_generator():
    # Тест на диапазоне от 1 до 5
    expected_output = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]
    assert list(generators.card_number_generator(1, 5)) == expected_output

    # Тест на диапазоне от 10010 до 10015
    expected_output_10000_to_10015 = [
        "0000 0000 0001 0010",
        "0000 0000 0001 0011",
        "0000 0000 0001 0012",
        "0000 0000 0001 0013",
        "0000 0000 0001 0014",
        "0000 0000 0001 0015"
    ]
    assert list(generators.card_number_generator(10010, 10015)) == expected_output_10000_to_10015

    # Тест на диапазоне от 0 до 0
    assert list(generators.card_number_generator(0, 0)) == ["0000 0000 0000 0000"]
