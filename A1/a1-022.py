day = int(input())
month = int(input())
lists = [
    [22,12,19,"capricorn"],
    [20,1,18,"aquarius"],
    [19,2,20,"pisces"],
    [21,3,19,"aries"],
    [20,4,20,"taurus"],
    [21,5,21,"gemini"],
    [22,6,22,"cancer"],
    [23,7,22,"leo"],
    [23,8,22,"virgo"],
    [23,9,23,"libra"],
    [24,10,21,"scorpio"],
    [22,11,21,"sagittarius"]
]

for l in lists:
    if (day >= l[0] and month == l[1]) or (day <= l[2] and month == (l[1]%12)+1):
        print(l[-1])
        break