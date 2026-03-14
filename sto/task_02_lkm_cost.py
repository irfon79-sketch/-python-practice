"""
Задача:
Посчитать стоимость базовой карски.

Вход:
grams_base
price_per_gram

Логика:
lkm_price = grams_base * price_per_gram

Выход:
lkm_price
"""


def calculate_lkm_price(grams_base, price_per_gram):
    lkm_price = grams_base * price_per_gram
    return lkm_price


result = calculate_lkm_price(150, 0.1)
print(result)
