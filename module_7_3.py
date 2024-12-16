import string


class WordsFinder:
    def __init__(self, *file_names):
        # Преобразуем входные аргументы в кортеж и сохраняем в атрибуте
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()  # Чтение файла в нижнем регистре

                    # Заменяем знаки препинания на пробелы
                    text = text.translate(str.maketrans('', '', string.punctuation))  # Убираем весь знак припинания

                    # Разбиваем текст на слова
                    words_list = text.split()
                    all_words[file_name] = words_list  # Добавляем в словарь

            except FileNotFoundError:
                # Обрабатываем ситуацию, если файл не найден
                print(f"Файл {file_name} не найден.")
                all_words[file_name] = []  # Записываем пустой список для отсутствующих файлов

        return all_words

    def find(self, word):
        results = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов

        for file_name, words in all_words.items():
            # Проверяем, есть ли слово в текущем файле
            if word.lower() in words:
                position = words.index(word.lower())  # Позиция первого вхождения
                results[file_name] = position + 1  # Номер слова (1 основание)

        return results

    def count(self, word):
        results = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов

        for file_name, words in all_words.items():
            # Считаем количество вхождений слова в текущем файле
            word_count = words.count(word.lower())
            results[file_name] = word_count

        return results


# Создание тестового файла
def create_test_file():
    with open('test_file.txt', 'w', encoding='utf-8') as file:
        content = """It's a text file.
For the task "найти везде" 
используйте его для самопроверки! 
Успехов в решении задачи.
Text text text"""
        file.write(content)


# Основной код для тестирования
if __name__ == "__main__":
    create_test_file()  # Создаем тестовый файл
    finder2 = WordsFinder('test_file.txt')

    # Получение всех слов из файла
    print(finder2.get_all_words())  # Все слова

    # Найти позицию слова 'text'
    print(finder2.find('text'))  # Позиция слова по счёту

    # Подсчет количества слова 'text'
    print(finder2.count('text'))  # Количество данного слова
