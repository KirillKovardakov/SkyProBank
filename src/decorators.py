# test_decorators.py
import functools
import logging


def log(filename=None):
    """Логирование начала и конца функции"""
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO, format='%(message)s')
    else:
        logging.basicConfig(level=logging.INFO, format='%(message)s')

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logging.info(f"{func.__name__} started")
                result = func(*args, **kwargs)
                logging.info(f"{func.__name__} result:{result}")
                logging.info(f"{func.__name__} ended")
                return result
            except Exception as e:
                logging.error(f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")
                raise  # повторное возбуждение исключения

        return wrapper

    return decorator
