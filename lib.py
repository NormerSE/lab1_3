def count_common_elements(*lists):
# Принимает списки и возвращает количество одинаковых элементов в них.
    # Преобразуем все списки в множества
    sets = [set(lst) for lst in lists]

    # Находим пересечение всех множеств
    common_elements = set.intersection(*sets)
    return len(common_elements)
# Пример