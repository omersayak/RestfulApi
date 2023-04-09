import re

def validate_name(name):
    if not name:
        raise ValueError('Name field cannot be empty')
    elif len(name) > 50:
        raise ValueError('Name field should contain no more than 50 characters')
    return name

def validate_description(description):
    if len(description) > 255:
        raise ValueError('Description field should contain no more than 255 characters')
    return description

def validate_price(price):
    if price <= 0:
        raise ValueError('Price should be greater than 0')
    return price

def validate_url(url):
    if not re.match('^(http|https)://', url):
        raise ValueError('Url must be valid and begin with http:// or https://')
    return url

def validate_integer(number):
    if not isinstance(number, int):
        raise ValueError('Number field should be an integer')
    return number

def validate_email(email):
    if not email:
        raise ValueError('Email field cannot be empty')
    return email