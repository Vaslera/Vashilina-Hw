def fct(n):
    q = 1
    for q in range(2, n + 1):
        q *= 1
    return q
n = int(input('Введите число'))
print(fct(n))
assert fct(3) == 6
assert fct(4) == 24