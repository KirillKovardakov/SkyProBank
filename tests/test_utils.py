import pytest
import tempfile
import os
import json
from src.utils import load_transactions


def test_file_not_exists():
    assert load_transactions("non_existing_file.json") == []


def test_valid_json_list():
    data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".json", encoding='utf-8') as tmp:
        json.dump(data, tmp)
        tmp_path = tmp.name
    try:
        assert load_transactions(tmp_path) == data
    finally:
        os.remove(tmp_path)


def test_json_not_a_list():
    data = {"id": 1, "amount": 100}
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".json", encoding='utf-8') as tmp:
        json.dump(data, tmp)
        tmp_path = tmp.name
    try:
        assert load_transactions(tmp_path) == []
    finally:
        os.remove(tmp_path)


def test_invalid_json():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".json", encoding='utf-8') as tmp:
        tmp.write("{ invalid json ]")
        tmp_path = tmp.name
    try:
        assert load_transactions(tmp_path) == []
    finally:
        os.remove(tmp_path)


def test_empty_file():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".json", encoding='utf-8') as tmp:
        tmp_path = tmp.name
    try:
        assert load_transactions(tmp_path) == []
    finally:
        os.remove(tmp_path)
