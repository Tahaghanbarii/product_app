import re


def price_validator(price):
    return bool(re.match(r"[0-9]\d{9}", price))

def name_validator(name):
    return bool(re.match(r"[a-zA-Z]{2-30}", name))