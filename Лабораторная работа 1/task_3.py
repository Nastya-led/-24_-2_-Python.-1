list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Определяем общее количество игроков
total_players = len(list_players)

# Определяем индекс
middle_index = total_players // 2

# Разделяем список
first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

# Печатаем команды
print(first_team)
print(second_team)
