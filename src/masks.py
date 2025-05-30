from typing_extensions import Union
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(funcName)s - %(levelname)s : %(message)s',
                    filename='../logs/masks.log',  # Запись логов в файл
                    filemode='w')
logger = logging.getLogger("app.masks")


def get_mask_card_number(card_numb: Union[str]) -> Union[str]:
    """Возвращает маску номера карты"""
    mask_card_numb = ""

    if card_numb == '' or card_numb is None or not isinstance(card_numb, str):
        logger.error("Не ввели карту")
        raise 'Введите карту'
    if not card_numb.isdigit() or len(card_numb) != 16:
        logger.error("Ввели неправильную карту!")
        raise 'Такой карты не существует!'
    else:
        logger.info("Cooking card number mask")
        for i, numb in enumerate(card_numb):
            if i % 4 == 0 and i != 0:
                mask_card_numb += " "
            if 6 <= i < 12:
                mask_card_numb += "*"
            else:

                mask_card_numb += numb
    logger.info("Maked card number mask")

    return mask_card_numb


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Возвращает маску номера счёта"""
    logger.info("Taking account number")
    mask_account = ''
    if isinstance(account_number, str):
        if account_number == '' or not account_number.isdigit() or len(account_number) != 20:
            logger.error(f'Incorrect account number: {account_number}')
            raise 'Такого номера счёта не существует!'
        mask_account = "**" + account_number[-4::]
    logger.info("Return mask of account number")
    return mask_account
