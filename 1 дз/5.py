print("Введите два числа")
x = int(input())
y = int(input())
if x == 0 or y == 0:
    print("Точка лежит на оси")
elif x > 0 and y > 0:
    print("Точка в первой четверти")
elif x > 0 and y < 0:
    print("Точка в четвертой четверти")
elif x < 0 and y > 0:
    print("Точка во второй четверти")
else:
    print("Точка в третей четверти")