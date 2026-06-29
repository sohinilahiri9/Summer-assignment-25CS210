# 1. Define the original array
arr = [10, 20, 30, 40, 50]
print("Original array:", arr)

# 2. Initialize two pointers
start = 0
end = len(arr) - 1

# 3. Loop until the pointers meet in the middle
while start < end:
    # Swap the elements at start and end
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    
    # Move pointers toward the center
    start = start + 1
    end = end - 1

# 4. Print the final reversed array
print("Reversed array:", arr)