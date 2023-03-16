import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def getname(self):

        """функция для получения значения атрибута name"""

        return self.__name

    @getname.setter
    def getname(self, name):

        """функция для изменения/определения атрибута name"""

        self.__name = name
        if len(self.__name) >= 10:
            print('Exception: Длина наименования товара превышает 10 символов.')
        else:
            return self.__name

    @classmethod
    def instantiate_from_csv(cls, csv_file='../src/items.csv'):

        """класс метод для получения данных из файла сsv и формирования экземпляров"""

        with open(csv_file, encoding='windows-1251') as file:
            reader = csv.DictReader(file, delimiter=',')
            for i in reader:
                name, price, quantity = i.get('name'), int(i.get('price')), int(i.get('quantity'))
                cls.all.append((name, price, quantity))

    @staticmethod
    def string_to_number(number: str) -> int:

        """функция, преобразующая строку в целое число"""

        return int(float(number))

