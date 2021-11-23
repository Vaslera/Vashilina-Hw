from h31 import mth


def tmth(a, b):
    for i in range(b):
        a = a[-1:] + a[:-1]
        return a
a = mth()
b = int(input('На сколько сместить'))
print(tmth(a, b))
assert tmth([1, 2, 3, 4, 5,], 1) == [5, 1, 2, 3, 4]
assert tmth([1, 2, 3, 4, 5,], 2) == [4, 5, 1, 2, 3]
assert tmth([1, 2, 3, 4, 5,], 3) == [3, 4, 5, 1, 2]