n = int(input())
data = []
vowel = ['A','E','I','O','U']

for i in range(n):
    data.append(input())
    
ans = 0
for d in data:
    if d in vowel:
        ans += 1

print(ans)
