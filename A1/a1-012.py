n1 = input()
op = input()
n2 = int(n1[::-1])
n1 = int(n1)
if op == '+':
    r = n1 + n2
elif op == '*':
    r = n1 * n2
print(f'{n1} {op} {n2} = {r}')
