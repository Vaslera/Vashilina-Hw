from h31 import mth


def counter():
    x = mth()
    for i in set(x):
        y = x.count(i)
        print('Элемент', i, '\t', '|', '\t',  'частота - ', y)


counter()