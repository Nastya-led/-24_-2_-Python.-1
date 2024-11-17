money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# Переменные
months = 0  # Счетчик месяцев

# Расчет
while money_capital + salary >= spend:  # Пока хватает денег
    money_capital = money_capital + salary - spend  # Остаток
    spend *= (1 + increase)  # Увеличиваем расходы
    months += 1  # Увеличиваем счетчик месяцев

print("Количество месяцев, которое можно протянуть без долгов:", months)
