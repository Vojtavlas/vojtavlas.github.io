count = 0
while True:
    x = int(input("Number of card: ")) # Convert input to integer
    if x in [2, 3, 4, 5, 6]:
        count -= 1
    elif x in [7, 8, 9, 10, 1, 11]:
        count += 1
    elif x == 69:
        print(count)
    else:
        print("Wrong number")
