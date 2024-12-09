

    # TODO Вызовите функцию, что получить индекс товараdef find_item_index(items, target_item):
def find_item_index(items, target_item):
# Напишите функцию для поиска индекса товара
    try:
        return items.index(target_item)
    except ValueError:
        return None

# Вызовем функцию
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    # Вызов функции для получения индекса товара
    index_item = find_item_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")