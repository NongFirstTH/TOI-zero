def checkStatus(temp, minT, maxT):
    if temp <= minT:
        return("solid")
    elif temp >= maxT:
        return("gas")
    else:
        return("liquid")
        
temp = int(input())
type = input().lower()

if type == 'c':
    print(checkStatus(temp, 0, 100))
else:
    print(checkStatus(temp, 32, 212))
    