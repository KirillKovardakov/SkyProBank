import pytest
import src.widget as widget


@pytest.mark.parametrize("input_data, expected_output", [
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 7922 **** 6361"),
    ("MasterCard 5133 3367 8910 1116", "MasterCard 5133 3367 **** 1116"),
    ("American Express 3782 8224 6310 005", ""),
    ("Дебетовая карта 1234 5678 9123 4567", "Дебетовая карта 1234 5678 **** 4567"),
])
def test_mask_account_card_valid_cases(input_data, expected_output):
    assert widget.mask_account_card(input_data) == expected_output


@pytest.mark.parametrize("input_data", ["", None, 123456, "Тест 123"])
def test_mask_account_card_invalid_cases(input_data):
    assert widget.mask_account_card(input_data) == ''


@pytest.mark.parametrize("input_data, expected_output", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-12-01T15:45:00.671407", "01.12.2023"),
    ("2020-01-31T15:45:00.671407", "31.01.2020"),
])
def test_get_date_valid(input_data, expected_output):
    assert widget.get_date(input_data) == expected_output


@pytest.mark.parametrize("input_data", [
    "", None, "11.03.2024", "2024-02-30T00:00:00", 12345, ])
def test_get_date_invalid(input_data):
    assert widget.get_date(input_data) == ""
