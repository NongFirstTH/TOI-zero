s = input()
k = []
for i in range(len(s)):
    t = s[i]
    if t not in k:
        c = s.count(t)
        print(c, end='')
        print(t, end='')
        k.append(t)