numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Шаг 1
filtered_numbers = [num for num in numbers if num is not None]
average = sum(filtered_numbers) / len(numbers)
# Шаг 2
numbers = [average if num is None else num for num in numbers]

# Выводим измененный список
print("Измененный список:", numbers)

