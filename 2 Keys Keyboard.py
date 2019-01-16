def minSteps(n):
    """
    :type n: int
    :rtype: int
    """
    result = 0
    diviser = 2
    while n > 1:
        while n % diviser == 0:
            result += diviser
            n /= diviser
        diviser += 1

    return result
