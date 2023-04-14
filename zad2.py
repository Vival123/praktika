a = [1, 4, 6]
b = [11, 33, 22]

# Создание словаря, ключи - 2 массив, а значения - 1 массив
d = {b[i]: a[i] for i in range(len(a))}

# Сортируем элементы 2 массива
b_sorted = sorted(b)

# Новый отсортированный массив
a_sorted = [d[x] for x in b_sorted]

print(a_sorted)