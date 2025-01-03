# TODO решите задачу

import json


def task() -> float:
    # Открываем файл с данными
    with open('data.json', 'r') as file:
        data = json.load(file)  # Загружаем JSON

    # Суммируем произведения
    total = sum(item['score'] * item['weight'] for item in data)

    # Возвращаем результат, округленный до 2 знаков
    return round(total, 2)


# Печатаем результат
print(task())
