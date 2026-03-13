"""
Задача:
Посчитать прибыль СТО с одной детали.

Вход:
client_price
master_percent
materials_percent

Логика:
materials_cost = client_price * materials_percent
labor_part = client_price - materials_cost
master_income = labor_part * master_percent
sto_profit = labor_part - master_income

Выход:
sto_profit
"""


def calculate_sto_profit(client_price, master_percent, materials_percent):
    materials_cost = client_price * materials_percent
    labor_part = client_price - materials_cost
    master_income = labor_part * master_percent
    sto_profit = labor_part - master_income
    return sto_profit


result = calculate_sto_profit(150, 0.5, 0.3)
print(result)
