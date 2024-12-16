def custom_write(file_name, strings):
    # Словарь для хранения позиций и строк
    strings_positions = {}

    # Открываем файл для записи
    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings):
            # Получаем текущую позицию в файле
            position = file.tell()
            # Записываем строку в файл с переходом на новую строку
            file.write(string + '\n')
            # Сохраняем информацию о позиции и строке в словаре
            strings_positions[(index + 1, position)] = string

    return strings_positions


# Пример выполняемого кода
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
