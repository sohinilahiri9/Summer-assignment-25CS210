def reverse_num(n, rev=0):
    if n == 0:  # base case
        return rev
    return reverse_num(n // 10, rev * 10 + n % 10)

num = int(input("Enter number: "))
print(f"Reverse of {num} = {reverse_num(num)}")