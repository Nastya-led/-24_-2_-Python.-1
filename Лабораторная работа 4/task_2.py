# TODO импортировать необходимые молули

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


    ...  # TODO считать содержимое csv файла

    def task() -> None:
        # Чтение содержимого CSV-файла
        with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)  # Читаем CSV как список словарей
            data = [row for row in reader]  # Преобразуем данные в список словарей

    ...  # TODO Сериализовать в файл с отступами равными 4

 # Сериализация данных в JSON с отступами равными 4
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)  # Запись в JSON с отступами


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, mode='r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end=""