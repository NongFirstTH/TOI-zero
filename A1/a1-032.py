def printStar(n):
    if n < 1:
        return
    else:
        print('*',end='')
        return printStar(n-1)

n = int(input())
for i in range(0,6,2):
    printStar(n-i)
    print()
