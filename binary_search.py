

def binary_search(array, low, high, x):
    if high < low:
        return -1
    else:
        middle = (low + high) // 2
        if array[middle] == x:
            return middle
        if array[middle] < x:
            return binary_search(array, middle + 1, high, x)
        if array[middle] > x:
            return binary_search(array, low, middle - 1, x)
print(binary_search([2, 4, 5, 7, 8], 0, 4, 4))


