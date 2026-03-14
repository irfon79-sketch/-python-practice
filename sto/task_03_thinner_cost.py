"""
Задача:
Посчитать стоимость разбавителя.

Вход:
base_cost
thinner_percent

Логика:
thinner_cost = base cost * thinner_percet


Выход:
thinner_cost

"""


def calculate_thinner_cost(base_cost, thinner_percent):
    thinner_cost = base_cost * thinner_percent
    return thinner_cost


result = calculate_thinner_cost(100, 0.3)
print(result)
