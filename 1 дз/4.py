print("Введите строку")
b = 0
k = 0
s = str(input())
k = len(s)
a = k
while (k != 0):
    k -= 1
    if s[0] == s[-1]:
        b += 1
s = (a / 2) - 1
if b > s:
    print("Палиндром")
else:
    print("Не палиндром")    
    