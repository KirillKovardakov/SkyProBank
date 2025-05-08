import src.processing as processing
import pytest


@pytest.mark.parametrize("test_state,  expected",
                         [('EXECUTED', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                          ('CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                        {'id': 615064591, 'state': 'CANCELED',
                                         'date': '2018-10-14T08:21:33.419441'}]), ])
def test_filter_by_state_basic(list_of_dict_fixture, test_state, expected):
    assert processing.filter_by_state(list_of_dict_fixture, test_state) == expected


def test_filter_by_state_none(list_of_dict_fixture):
    assert processing.filter_by_state(list_of_dict_fixture) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_sort_by_date_basic(list_of_dict_fixture, list_of_dict_reversed_fixture, list_of_dict_not_reversed_fixture):
    assert processing.sort_by_date(list_of_dict_fixture, True) == list_of_dict_reversed_fixture
    assert processing.sort_by_date(list_of_dict_fixture, False) == list_of_dict_not_reversed_fixture
    assert processing.sort_by_date(list_of_dict_fixture) == list_of_dict_reversed_fixture


def test_filter_by_state_invalid(list_of_dict_fixture):
    with pytest.raises(ValueError):
        processing.filter_by_state([])
    with pytest.raises(ValueError):
        processing.filter_by_state(list_of_dict_fixture, 'True')


def test_sort_by_date_invalid(list_of_dict_fixture):
    with pytest.raises(ValueError):
        processing.sort_by_date([])
    with pytest.raises(ValueError):
        processing.sort_by_date(list_of_dict_fixture, 'True')
