salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
def calculate_safety_cushion(salary, spend, months, increase):
    money_capital = 0  # Начальное значение подушки безопасности
    for _ in range(months):
        # Покрытие зп
        deficit = spend - salary
        if deficit > 0:
            # Покрытие подушкой
            money_capital += deficit
        # Увеличиваем расходы на следующий месяц
        spend *= (1 + increase)
    return round(money_capital)
money_capital = calculate_safety_cushion(salary, spend, months, increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)