while True:
    d = int(input('Enter the number above 0: '))
    if d <= 0:
        continue
    else:
        # code goes here
        binary = ""
        while True:
            r = d % 2
            if r == 1:
                binary = f"1{binary}"
            else:
                binary = f"0{binary}"

            d = d//2
            if d != 0:
                continue
            else:
                print(binary)
                break
        break
