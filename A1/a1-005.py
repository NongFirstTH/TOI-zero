m = int(input())
d = int(input())
s = ["winter", "spring", "summer", "fall"]
if m % 3 == 0 and d >= 21:
    idx = ((m+1)%12)//3
    print(s[idx])
else:
    print(s[m//3])