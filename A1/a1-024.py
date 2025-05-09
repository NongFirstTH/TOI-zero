def tax(data):
    if cc <= 1500:
        return data[0]
    elif 1500 < cc <= 2000:
        return data[1]
    else:
        return data[2]
        
year = int(input())
cc =int(input())
data = [
    [1250,1400,2000],
    [1100,1300,1700],
    [1000,1200,1500]
]
if year <= 1990:
    print(tax(data[0]))
elif 1991 <= year <= 1999:
    print(tax(data[1]))
else:
    print(tax(data[2]))