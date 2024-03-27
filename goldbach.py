
def is_prime(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

def goldbach(m):
    for j in range(2, m):
        if is_prime(j) == 1 and is_prime(m - j) == 1:
            return (j, m - j)
    return f'Goldbach\'s conjecture is wrong!!!'
for k in range(4, 102, 2):
    print(k, ':', goldbach(k))


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def goldbach(m):
    for j in range(2, m):
        if is_prime(j) == True and is_prime(m - j) == True:
            return (j, m - j)
    return f'Goldbach\'s conjecture is wrong!!!'
for k in range(4, 204, 2):
    print(k, ':', goldbach(k))
