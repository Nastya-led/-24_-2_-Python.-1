# TODO Напишите функцию find_common_participants
# Функция для поиска общих участников
def find_common_participants(group1, group2, delimiter=","):
    # Разделяем строки на 2 списка
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))
    # Находим пересечение двух множеств и сортируем результат
    common_participants = sorted(participants1 & participants2)
    return common_participants

# Две группы участников с разделителем ","


participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой

# Проверка работы функции с разделителем по умолчанию
result = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", result)

# Проверка работы функции с другим разделителем "|"
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print("Общие участники с разделителем '|':", result)
