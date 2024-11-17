salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# Переменные
required_capital = 0  # Необходимая подушка безопасности

# Расчет
for _ in range(months):
    deficit = spend - salary  # Нехватка средств за месяц
    if deficit > 0:
        required_capital += deficit  # Увеличиваем необходимую подушку безопасности
    spend *= (1 + increase)  # Увеличиваем расходы

# Округляем до целого числа
required_capital = round(required_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {required_capital}")
