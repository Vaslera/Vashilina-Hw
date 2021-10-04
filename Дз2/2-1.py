print("Введите элемент")
a = list(input())
while (a[-1] != " "):
    a += input()
a.remove(" ")
print(a)