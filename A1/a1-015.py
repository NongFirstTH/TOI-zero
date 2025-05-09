f = input()
l = input()
y = input()
if len(f) > 5 and len(l) > 5:
    print(f[0:2]+l[-1]+y[-1])
else:
    print(f[0]+y+l[-1])