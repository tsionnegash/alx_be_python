i = 0
number = int(input("Enter the size of the pattern: "))
while i < number:
    for number in range(1, number+1):
        print("*", end="")

    print()
    i += 1