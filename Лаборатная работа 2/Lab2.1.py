# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
# Исходные данные
money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

def calculate_months(money_capital, salary, spend, increase):
    months = 0
    while money_capital >= 0:
        # Вычитаем расходы из текущего бюджета
        money_capital += salary - spend
        # Проверяем, если деньги закончились
        if money_capital < 0:
            break
        # Увеличиваем расходы на 5%
        spend *= (1 + increase)
        months += 1
    return months
# Расчет
months = calculate_months(money_capital, salary, spend, increase)

print("Количество месяцев, которое можно протянуть без долгов:", months)
