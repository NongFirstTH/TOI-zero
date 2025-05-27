n = int(input())
data = []

for i in range(n):
    data.append(int(input()))

if len(data) != 0:
    ans = min(data)
    print(ans)