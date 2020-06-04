class Menu(object):

    def __init__(self):
        self.__choice = 0
        self.__answer = 'n'

    @staticmethod
    def display() -> None:
        print('=======================================')
        print('  Система управления каталогом товаров ')
        print('=======================================')
        print('   1 - Показать список категорий       ')
        print('   2 - Выборка по категориям           ')
        print('   3 - Показать список производителей  ')
        print('   4 - Выборка по производителям       ')
        print('   5 - Выборка по ценам                ')
        print('   6 - Добавить категорию              ')
        print('   7 - Удалить категорию               ')
        print('   8 - Добавить производителя          ')
        print('   9 - Удалить производителя           ')
        print('  10 - Добавить товар                  ')
        print('  11 - Удалить товар                   ')
        print('  12 - Изменить цену товара            ')
        print('=======================================')

    def allow_continue(self) -> bool:
        self.__answer = input('Продолжать (y/n)? - ')
        return self.__answer == 'y' or self.__answer == 'Y'

    def get_choice(self) -> int:
        while True:
            try:
                self.__choice = int(input('Выберите нужное действие: '))
                return self.__choice
            except ValueError:
                print('Неправильный формат ввода!')
