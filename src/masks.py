from typing_extensions import Union


def get_mask_card_number(card_numb: Union[str]) -> Union[str]:
    """Возвращает маску номера карты"""
    str_card_numb = str(card_numb)
    mask_card_numb = ""
    for i, numb in enumerate(str_card_numb):
        if i % 4 == 0:
            mask_card_numb += " "
        if i >= 6 and i < 12:
            mask_card_numb += "*"
        else:
            mask_card_numb += numb
    return mask_card_numb


def get_mask_account(card_numb: Union[str]) -> Union[str]:
    """Возвращает маску номера счёта"""
    mask_card_numb = str(card_numb)
    return "**" + mask_card_numb[-4::]
