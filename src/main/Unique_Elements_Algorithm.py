def unique_elements(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return False
    return True

# Example usage:
my_array = [1, 2, 3, 4, 5]
result = unique_elements(my_array)
print(result)

my_array2 = [1, 2, 3, 2, 4, 5]
result2 = unique_elements(my_array2)
print(result2)