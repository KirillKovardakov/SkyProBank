from src.decorators import log
import os
import datetime
import pytest
from time import time


def test_log(capsys):
    @log('filename.txt')
    def add_numbers_with_filename(x, y):
        return x + y

    result = add_numbers_with_filename(3, 5)
    assert result == 8

    @log()
    def add_numbers_without_filename(x, y):
        print(x + y)

    add_numbers_without_filename(5, 2)
    captured = capsys.readouterr()
    assert captured.out == "7\n"


def test_log_exceptions():
    @log()
    def function_exception(x, y):
        raise Exception("Something went wrong!")

    with pytest.raises(Exception, match="Something went wrong!"):
        function_exception(1, 2)

    @log('filename.txt')
    def function_exception(x, y):
        raise Exception("Something went wrong!")

    with pytest.raises(Exception, match="Something went wrong!"):
        function_exception(1, 2)
