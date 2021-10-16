print("Введите выражение")
s = input()
a = s.count('(')
b = s.count(')')
if a > b:
    print('Не хватает ', a - b, 'закрывающих скобок')
elif a < b:
    print('Не хватает ', b - a, 'открывающих скобок')
else:
    print('Все верно')