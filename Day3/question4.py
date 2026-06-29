a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

lcm = abs(a * b) // gcd(a, b)
print(f"LCM of {a} and {b} is {lcm}")