print("Введите строку")
a = input()
b = []
print("Введите число")
k = int(input())
for i in a:
    if i.isdigit():
       b.append(i)
print(k, '-ая цифра в строке', b[k - 1])