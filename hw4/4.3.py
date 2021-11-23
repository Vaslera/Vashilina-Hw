from h31 import mth
def a(y):
    s = list(y)
    if y == s:
        return "True"
    else:
        return "False"
y = b()
print(a(y))
assert a(1, 2, 3, 4, 5, 6, 7) == "True"
assert a(1, 2, 1, 4, 2, 6, 7) == "False"