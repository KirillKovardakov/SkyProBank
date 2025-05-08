import pytest


@pytest.fixture
def wrong_cards_fixture() -> tuple:
    return 7000792289606361, [7365410843013587], {'7365410843013587', }, '7390', '7654p1p843j13587',
    '7654p1p84k3j135;87', '736541084301358', '', '73654108430135874305080', None


@pytest.fixture
def wrong_numbs_fixture() -> tuple:
    return '73654108430j35875642', '32', 4234, '3412412312312412355', '', None


@pytest.fixture
def list_of_dict_fixture() -> list[dict]:
    return ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])


@pytest.fixture
def list_of_dict_reversed_fixture() -> list[dict]:
    return ([{'date': '2019-07-03T18:35:29.512364', 'id': 41428829, 'state': 'EXECUTED'},
             {'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'},
             {'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
             {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}])


@pytest.fixture
def list_of_dict_not_reversed_fixture() -> list[dict]:
    return ([{'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'},
             {'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
             {'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'},
             {'date': '2019-07-03T18:35:29.512364', 'id': 41428829, 'state': 'EXECUTED'}])
