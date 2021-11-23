def fibonacci(s):
    x = [0, 1]
    for i in range(2, s + 1):
        b = x[i-1] + x[i-2]
        x.append(b)
    print(x)
    return x