from lib.models import Product, Category, Catalog
from pickle import dump, load
from lib.assistent import Menu
from lib.controllers import MainController


if __name__ == '__main__':

    m = Menu()
    mc = MainController()
    while True:
        m.display()
        k = m.get_choice()
        if k == 1:
            mc.display_categories()
        elif k == 2:
            mc.select_by_category()
        elif k == 3:
            pass
        elif k == 4:
            pass
        elif k == 5:
            pass
        elif k == 6:
            pass
        elif k == 7:
            pass
        elif k == 8:
            pass
        elif k == 9:
            pass
        elif k == 10:
            pass
        elif k == 11:
            pass
        elif k == 12:
            pass
        else:
            print('Вы выбрали несуществующий вариант!')
        if not m.allow_continue():
            break
    print('Программа завершена')
