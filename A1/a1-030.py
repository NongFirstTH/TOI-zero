n = int(input())
nums = input().split()
nums = [int(x) for x in nums]
lnums = len(nums)

if lnums == 2:
    print(max(nums))
else:
    sum = 0
    for i in range(1,lnums,2):
        maxNum = max(nums[i-1],nums[i])
        sum += maxNum
        print(f'{maxNum}', end='')
        if i != lnums-1:
            print(' + ', end='')
        else:
            print(' = ', end='')
           
    print(sum)