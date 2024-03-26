

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


def binary_search(array, kam, ziad, x):
    if ziad < kam:
        return -1
    else:
        vasat = (kam + ziad) // 2
        if array[vasat] == x:
            return vasat
        if array[vasat] < x:
            return binary_search(array, vasat + 1, ziad, x)
        if array[vasat] > x:
            return binary_search(array, kam, vasat - 1, x)
print(binary_search([2, 4, 5, 7, 8], 0, 4, 7))
