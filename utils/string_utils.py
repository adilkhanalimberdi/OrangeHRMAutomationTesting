import string
from random import randint, choice


def get_random_symbols(length):
    uppers = string.ascii_uppercase
    lowers = string.ascii_lowercase
    digits = list(string.digits)

    upper_num = randint(1, 3)
    digit_num = randint(1, 3)
    res_upp = [choice(uppers) for _ in range(upper_num)]
    res_low = [choice(lowers) for _ in range(abs(length - upper_num - digit_num))]
    res_dig = [choice(digits) for _ in range(digit_num)]

    return "".join(res_upp + res_low + res_dig)