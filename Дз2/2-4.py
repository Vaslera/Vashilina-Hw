print("Введите выражение")
s = list(input())
for i in s:
    a = s.count('(')
    b = s.count(')')
if a > b:
    print('Не хватает ', a - b, 'закрывающих скобок')
elif a < b:
    print('Не хватает ', b - a, 'открывающих скобок')
else:
    print('Все верно')