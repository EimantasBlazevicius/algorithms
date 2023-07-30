def factorial(n):
    """Calculates factorial in an iterative manner.

    Args:
        n: the natural number that is the input for the algorithm.
    Returns:
        factorial of number n.
    """
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


print(factorial(5))


def factorial_rec(n):
    """Calculates factorial in a recursive manner.

    Args:
        n: the natural number that is the input for the algorithm.
    Returns:
        factorial of number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n-1)


print(factorial_rec(159))
