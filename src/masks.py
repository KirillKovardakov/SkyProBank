from typing_extensions import Union


def get_mask_card_number(card_numb: Union[str]) -> Union[str]:
    """Возвращает маску номера карты"""
    mask_card_numb = ""

    if card_numb == '' or card_numb is None or not isinstance(card_numb, str):
        raise 'Введите карту'
    if not card_numb.isdigit() or len(card_numb) != 16:
        raise 'Такой карты не существует!'
    else:
        for i, numb in enumerate(card_numb):
            if i % 4 == 0 and i != 0:
                mask_card_numb += " "
            if 6 <= i < 12:
                mask_card_numb += "*"
            else:
                mask_card_numb += numb
    return mask_card_numb


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Возвращает маску номера счёта"""
    mask_account = ''
    if isinstance(account_number, str):
        if account_number is None or account_number == '' or not account_number.isdigit() or len(account_number) != 20:
            raise 'Такого номера счёта не существует!'
        mask_account = "**" + account_number[-4::]
    return mask_account
