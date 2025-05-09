n1 = int(input())
n2 = int(input())
n3 = int(input())
s = {n1, n2, n3}
l = len(s)
if l == 1:
    print("all the same")
elif l == 2:
    print("neither")
else:
    print("all different")