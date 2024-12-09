# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter=","):

    # Разделение строк на списки участников
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))

    # Поиск пересечения и сортировка
    return sorted(participants1 & participants2)

# Вызов функции
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print("Общие участники:", common_participants)
