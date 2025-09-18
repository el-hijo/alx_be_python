size = int(input("Enter the size of the pattern: "))
outer = 0
while outer < size:
    inner = 0
    while inner < size:
        print("*", end = " ")
        inner += 1
    print()
    outer += 1