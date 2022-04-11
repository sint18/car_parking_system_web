import hashlib
import math


def get_hash(text):
    if text:
        res = hashlib.sha256(text.encode()).hexdigest()
        return res


def calculate_fees(hours: float, rate1: int, rate2: int):
    total_hr = math.ceil(hours)
    res = 0
    if total_hr == 1:
        res = rate1
    if total_hr > 1:
        res = ((total_hr - 1) * rate2) + rate1
    return res


def format_currency(currency: int):

    try:
        res = "{:,} MMK".format(currency)
        return res
    except TypeError:
        return 0


def test_ceil(h):
    return math.ceil(h)
