import pytest

import src.masks as masks


@pytest.mark.parametrize("my_card, expected",
                         [('7000792289606361', '7000 79** **** 6361'),
                          ('7365410843013587', '7365 41** **** 3587')])
def test_get_mask_card_number_basic(my_card, expected):
    assert masks.get_mask_card_number(my_card) == expected


def test_get_mask_card_number_invalid(wrong_cards_fixture):
    with pytest.raises(TypeError):
        masks.get_mask_card_number(wrong_cards_fixture)
    with pytest.raises(TypeError):
        masks.get_mask_card_number('')
    with pytest.raises(TypeError):
        masks.get_mask_card_number('hkl98l8')
    with pytest.raises(TypeError):
        masks.get_mask_card_number(None)


@pytest.mark.parametrize("my_account_numb, expected",
                         [('73654108430135874305', '**4305'),
                          ('73654108430135875642', '**5642')])
def test_get_mask_account_basic(my_account_numb, expected):
    assert masks.get_mask_account(my_account_numb) == expected


def test_get_mask_account_invalid(wrong_numbs_fixture):
    with pytest.raises(TypeError):
        masks.get_mask_account('73654108430j35875642')
    with pytest.raises(TypeError):
        masks.get_mask_account('')
    with pytest.raises(TypeError):
        masks.get_mask_account('yt67r6')
