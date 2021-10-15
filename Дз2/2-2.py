print("Введите строку")
b = input()
a = []
while (b != " "):
    a.append(b)
    b = input()
a.sort()
a = a[::-1]
print(*a, sep='')