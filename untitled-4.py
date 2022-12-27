def f(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2 and n % 3 == 0:
        return 2*n - f(n - 1) - f(n//3)
    else:
        return n + f(n - 2) + f(n // 10)
count = 0
for i in range(50, 101):
    F = f(i)
    if F > 50 and F <= 200:
        count += 1
        print(count)

    