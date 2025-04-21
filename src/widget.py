from datetime import datetime

from typing_extensions import Union


def mask_account_card(card_numb: Union[str]) -> Union[str]:
    """Возвращает маску номера карты"""
    mask_card_numb = ""
    count_to_space = 0
    if "Счет" in card_numb or "Счёт" in card_numb:
        return "Счет **" + card_numb[-4::]
    for i, numb in enumerate(card_numb):
        if numb.isdigit():
            if count_to_space % 4 == 0:
                mask_card_numb += " "
            count_to_space += 1
        if i >= (len(card_numb) - 10) and i < (len(card_numb) - 4):
            mask_card_numb += "*"
        else:
            mask_card_numb += numb
    return mask_card_numb


def get_date(date_str: Union[str]) -> Union[str]:
    """Преобразуем строку в объект datetime"""
    dt = datetime.fromisoformat(date_str)
    formatted_date = dt.strftime("%d.%m.%Y")

    return f'"{formatted_date}" ("{formatted_date}")'
