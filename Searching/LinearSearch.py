def LinearSear(arr,n, key):
    for i in range(n):
        if arr[i] == key:
            return i
    return -1
arr= [1, 2, 3, 4, 5]
key = 3
n = len(arr)
result = LinearSear(arr, n, key)
print("Element found at index:", result) if result != -1 else print("Element not found")
# Time complexity: O(n) where n is the number of elements in the array
result = LinearSear(arr, n, 15)
print("Element found at index:", result) if result != -1 else print("Element not found")
# Time complexity: O(n) where n is the number of elements in the array