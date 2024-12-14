class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()  # Удаляем лишние пробелы и пустые строки
        except FileNotFoundError:
            return ""  # Если файл не существует, возвращаем пустую строку

    def add(self, *products):
        existing_products = self.get_products().split('\n') if self.get_products() else []
        existing_names = {product.split(', ')[0] for product in
                          existing_products}  # Получаем имена существующих продуктов

        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name in existing_names:
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    file.write(str(product) + '\n')  # Записываем продукт в файл
                    print(f'Добавлен: {product}')


# Пример работы программы
if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')  # Дубликат

    print(p2)  # Вывод: Spaghetti, 3.4, Groceries

    # Первый запуск добавления продуктов
    s1.add(p1, p2, p3)

    print("\nТовары в магазине:")
    print(s1.get_products())

    # Второй запуск добавления тех же продуктов
    s1.add(p1, p2, p3)

    print("\nТовары в магазине после повторного добавления:")
    print(s1.get_products())
