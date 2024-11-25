import re

def name_validator(name):
    return bool(re.match(r"[a-zA-Z]{2-30}", name))

def brand_validator(brand):
    return bool(re.match(r"[a-zA-Z]{2-30}", brand))

