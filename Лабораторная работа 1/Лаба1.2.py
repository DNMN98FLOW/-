# TODO Найдите количество книг, которое можно разместить на дискете
# Дано
pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4
disk_size_mb = 1.44

# Переводим объем дискеты в байты
disk_size_bytes = disk_size_mb * 1024 * 1024

# Вычисляем объем одной книги в байтах
book_size_bytes = pages * lines_per_page * chars_per_line * bytes_per_char

# Вычисляем, сколько книг поместится на дискету
books_on_disk = disk_size_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", int(books_on_disk))
