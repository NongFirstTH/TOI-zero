c = input()
num = int(input())
if c == 'H':
    if num == 4567:
        print("safe unlocked")
    else:
        print("safe locked - change digit")
else:
    if num == 4567:
        print("safe locked - change char")
    else:
        print("safe locked")