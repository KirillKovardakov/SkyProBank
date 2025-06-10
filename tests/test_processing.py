from src.processing import filter_by_description,filter_by_state_re,filter_by_state,sort_by_date
import pytest


@pytest.mark.parametrize("test_state,  expected",
                         [('EXECUTED', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                          ('CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                        {'id': 615064591, 'state': 'CANCELED',
                                         'date': '2018-10-14T08:21:33.419441'}]), ])
def test_filter_by_state_basic(list_of_dict_fixture, test_state, expected):
    assert filter_by_state(list_of_dict_fixture, test_state) == expected


def test_filter_by_state_none(list_of_dict_fixture):
    assert filter_by_state(list_of_dict_fixture) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_sort_by_date_basic(list_of_dict_fixture, list_of_dict_reversed_fixture, list_of_dict_not_reversed_fixture):
    assert sort_by_date(list_of_dict_fixture, True) == list_of_dict_reversed_fixture
    assert sort_by_date(list_of_dict_fixture, False) == list_of_dict_not_reversed_fixture
    assert sort_by_date(list_of_dict_fixture) == list_of_dict_reversed_fixture


def test_filter_by_state_invalid(list_of_dict_fixture):
    with pytest.raises(ValueError):
        filter_by_state([])
    with pytest.raises(ValueError):
        filter_by_state([], 'True')


def test_sort_by_date_invalid(list_of_dict_fixture):
    with pytest.raises(ValueError):
        sort_by_date([])
    with pytest.raises(ValueError):
        sort_by_date(list_of_dict_fixture, 'True')
    with pytest.raises(ValueError):
        sort_by_date([], 'True')


def test_filter_by_state_re_basic(list_of_transactions_fixture):
    result = filter_by_state_re(list_of_transactions_fixture, "перевод организации")
    assert isinstance(result, list)
    assert len(result) == 2
    assert all("перевод организации" in tx["description"].lower() for tx in result)

def test_filter_by_state_re_case_insensitive(list_of_transactions_fixture):
    result = filter_by_state_re(list_of_transactions_fixture, "ОрГаНиЗаЦиИ")
    assert len(result) == 2

def test_filter_by_state_re_no_match(list_of_transactions_fixture):
    result = filter_by_state_re(list_of_transactions_fixture, "неизвестное описание")
    assert result == []


def test_filter_by_description_multiple_categories(list_of_transactions_fixture):
    categories = ["на карту", "на счет"]
    result = filter_by_description(list_of_transactions_fixture, categories)
    assert result == {
        "Перевод с карты на карту": 1,
        "Перевод со счета на счет": 2
    }

def test_filter_by_description_no_match(list_of_transactions_fixture):
    categories = ["покупка"]
    result = filter_by_description(list_of_transactions_fixture, categories)
    assert result == {}