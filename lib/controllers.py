from lib.models import Catalog
import pickle


class MainController(object):

    def __init__(self):
        self.__catalog = Catalog('-')
        self.__storage = 'catalog.dat'
        self.load_data()

    def load_data(self) -> None:
        with open(self.__storage, 'rb') as f:
            self.__catalog = pickle.load(f)

    def save_data(self) -> None:
        with open(self.__storage, 'wb') as f:
            pickle.dump(self.__catalog, f)

    def display_categories(self) -> None:
        categories_list = self.__catalog.get_types()
        count = 0
        for category in categories_list:
            count += 1
            print(f'{count}. {category.get_name()}')

    def select_by_category(self) -> None:
        category = input('Введите название категории: ')
        pos = self.__catalog.find_category(category)
        if pos == -1:
            print(f'Категория {category} - не найдена!')
        else:
            self.__catalog.get_types()[pos].display()
