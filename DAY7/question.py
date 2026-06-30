def fibonacci(n):
    if n <= 1:  # base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # recursive call

n = int(input("Enter terms: "))
print(f"Fibonacci series:")
for i in range(n):
    print(fibonacci(i), end=" ")