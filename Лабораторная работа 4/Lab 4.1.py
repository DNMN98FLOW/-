# TODO решите задачу
import json
def task() -> float:
    with open('input.json') as file:
        data = json.load(file)

    # Суммируем произведения
    result = sum(item['score'] * item['weight'] for item in data)

    # Возвращаем результат, округленный до 3 знаков после запятой
    return round (result, 3)

# Выводим результат
print(task())
