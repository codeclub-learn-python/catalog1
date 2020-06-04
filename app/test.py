import pickle

# Temp Test-1:
# ============
"""
    p1 = Product('Колбаса докторская', 'Фирма Свитанок', 120.45)
    p2 = Product('Молоко витаминное', 'Веселый фермер', 17.15)
    p3 = Product('Торт Пражский', 'Кондитерская фабрика', 250.05)
    print(p1)
    p4 = Product('Гантели', 'Спорт-Майдан', 500.0)
    p5 = Product('Штанга', 'Спорт-Лайф', 800.0)
    p6 = Product('Ласты', 'Аква', 120.0)
    """

# Temp Test-2:
# ============
"""
    c1 = Category('Продукты питания')
    c1.add_product(p1)
    c1.add_product(p2)
    c1.add_product(p3)
    k = c1.find_product('Торт Пражский')
    print(k)
    c2 = Category('Спорттовары')
    c2.add_product(p4)
    c2.add_product(p5)
    c2.add_product(p6)
    """

# Temp Test-3:
# ============
# c1.display()
# c1.del_product('Молоко витаминное')
# c1.display()

# Temp Test-4:
# ============
"""
    catalog = Catalog('Мой каталог - 2020')
    catalog.add_category(c1)
    catalog.add_category(c2)
    catalog.display()
    """

# Temp Test-5:
# ============
"""
    with open('catalog.dat', 'wb') as f:
        dump(catalog, f)
    print('\n> Данные успешно сериализованы!')
    """

# Temp Test-6:
# ============
with open('catalog.dat', 'rb') as f:
    catalog_clone = pickle.load(f)
print('\n> Данные успешно десериализованы!')
catalog_clone.display()
