from datetime import datetime

from typing_extensions import Union


def mask_account_card(card_numb: Union[str]) -> Union[str]:
    """Возвращает маску номера карты"""
    mask_card_numb = ""
    count_to_space = 0
    if isinstance(card_numb, str):
        if len(card_numb) == 0 or card_numb == None:
            return ''
        else:
            if "Счет" in card_numb or "Счёт" in card_numb:
                return "Счет **" + card_numb[-4::]
            split_card_numb = card_numb.split()
            card_numb_without_name = ''.join([part for part in split_card_numb if part.isdigit()])
            mask_card_numb += ' '.join([part for part in split_card_numb if part.isalpha()]) + ' '
            if len(card_numb_without_name) != 16:
                return ''
            for i, numb in enumerate(card_numb_without_name):
                if numb.isdigit():
                    if count_to_space % 4 == 0 and count_to_space != 0:
                        mask_card_numb += " "
                    count_to_space += 1
                if (len(card_numb_without_name) - 8) <= i < (len(card_numb_without_name) - 4):
                    mask_card_numb += "*"
                else:
                    mask_card_numb += numb
    return mask_card_numb


def get_date(date_str: Union[str]) -> Union[str]:
    """Преобразуем строку в объект datetime"""
    try:
        dt = datetime.fromisoformat(date_str)
        formatted_date = dt.strftime("%d.%m.%Y")
        return formatted_date
    except (ValueError, TypeError):
        return ""
