def isPerfectSquare(num):
    counter = 0
    while counter * counter <= num:
        if counter * counter == num:
            return True

        counter += 1
    
    return False

print(isPerfectSquare(16))
print(isPerfectSquare(15))
print(isPerfectSquare(0))
print(isPerfectSquare(1))
