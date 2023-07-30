def recursion(number):
    if number != 0:
        number -= 1
        recursion(number)
    return 0


recursion(5)
