n = int(input("Enter n: "))

a, b = 0, 1
if n == 1:
    print(f"{n}th Fibonacci term is {a}")
elif n == 2:
    print(f"{n}th Fibonacci term is {b}")
else:
    for i in range(3, n + 1):
        a, b = b, a + b
    print(f"{n}th Fibonacci term is {b}")