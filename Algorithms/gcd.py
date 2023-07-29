a = int(input("enter number 1: "))
b = int(input("enter number 2: "))

while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print(a)
