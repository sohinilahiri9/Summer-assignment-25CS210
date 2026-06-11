num = int(input("Enter a number: "))
largest = 1
n = num

# Divide by 2 first
while n % 2 == 0:
    largest = 2
    n //= 2

# Check odd factors
i = 3
while i * i <= n:
    while n % i == 0:
        largest = i
        n //= i
    i += 2

# If remaining n is prime
if n > 2:
    largest = n

print(f"Largest prime factor of {num} is {largest}")