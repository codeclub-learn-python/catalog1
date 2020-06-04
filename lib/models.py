class Product(object):

    def __init__(self, name: str, producer: str, price: float):
        self.__name = name
        self.__producer = producer
        self.__price = price

    def get_name(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return f'{self.__name} / {self.__producer} - {self.__price:.2f} uah'


class Category(object):

    def __init__(self, name: str):
        self.__name = name
        self.__goods = list()

    def get_name(self) -> str:
        return self.__name

    def add_product(self, p: Product) -> None:
        if self.find_product(p.get_name()) == -1:
            self.__goods.append(p)

    def find_product(self, name: str) -> int:
        index = -1
        for p in self.__goods:
            index += 1
            if p.get_name() == name:
                return index
        return -1

    def del_product(self, name: str) -> None:
        index = self.find_product(name)
        if index != -1:
            del self.__goods[index]

    def display(self) -> None:
        print(f'\n> Категория: {self.__name}')
        print('-----------------------------')
        for p in self.__goods:
            print(p)


class Catalog(object):

    def __init__(self, name: str):
        self.__name = name
        self.__types = list()

    def get_types(self):
        return self.__types

    def add_category(self, c: Category) -> None:
        if self.find_category(c.get_name()) == -1:
            self.__types.append(c)

    def find_category(self, name: str) -> int:
        index = -1
        for c in self.__types:
            index += 1
            if c.get_name() == name:
                return index
        return -1

    def del_category(self, name: str) -> None:
        index = self.find_category(name)
        if index != -1:
            del self.__types[index]

    def display(self) -> None:
        print(f'\n> Каталог: {self.__name}')
        print('===============================')
        for c in self.__types:
            c.display()
