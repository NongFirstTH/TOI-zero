y = int(input())
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) or y == 1500:
    print("yes")
else:
    print("no")