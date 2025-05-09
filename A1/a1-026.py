a = int(input())
b = int(input())
c = int(input())

l = [a, b, c]
even = 0
odd = 0
for x in l:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
print("even", even)
print("odd", odd)