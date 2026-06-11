# Function to find max
def find_max(x, y):
    if x > y:
        return x
    else:
        return y

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Maximum =", find_max(a, b))