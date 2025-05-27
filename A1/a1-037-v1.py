import math

def expandNum(num):
    r = 10**int(math.log10(num))
    expand = (num // r) * r
    remain = num % r
    
    return expand, remain

def roman(romans, number, ans):
    for r in romans:
        # base case
        if number == 0:
            break
            
        # inductive case 
        # case 1 - 3
        if r == 1 and number <= 3:
            ans += romans[r]*number
        else:
            if number > 9:
                num, remain = expandNum(number)
            else:
                num = number
            
            # case num == r
            if num == r:
                ans += romans[r]
                
            # case num divisible by r
            elif num % r == 0 and num not in [40, 50, 90, 400, 500, 900]:
                ans += romans[r]*(num // r)

            # special case
            if num >= 400:
                if num == 400:
                    ans += 'CD'
                elif num == 900:
                    ans += 'CM'
                elif 600 <= num and r == 500:
                    ans += 'D'
            elif 40 <= num <= 399:
                if num == 90:
                    ans += 'XC'
                elif num == 40 and r == 10:
                    ans += 'XL'
                elif 60 <= num <= 80 and r == 50:
                    ans += 'L'
            elif 4 <= num <= 39:
                if num == 4:
                    ans += 'IV'
                    break
                elif num == 9:
                    ans += 'IX'
                    break
                elif 6 <= num <= 8:
                    ans += 'V'+'I'*(num-5)
                    break
                
            if 90 <= number < 100 or 400 <= number < 500 or 900 <= number:
                number = remain
            else:
                number %= r
            
    return ans

num = int(input())
romans = {
    1000:'M',
    500:'D', 
    100:'C', 
    50:'L', 
    10:'X',
    5:'V', 
    1:'I'
    }
ans = ''
print(roman(romans, num, ans))
