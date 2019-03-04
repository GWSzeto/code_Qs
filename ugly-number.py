def isUgly(num):
    if num < 0:
        return False

    for prime in [2,3,5]:
        while num % prime == 0:
            num /= prime

    return num == 1

print(isUgly(6))
print(isUgly(8))
print(isUgly(14))


