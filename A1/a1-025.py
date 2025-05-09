card = input()
suit = card[-1]
num = card.split(suit)[0].upper()
suits = {'D':"diamonds", 'H':"hearts", 'S': "spades", "C": 'clubs'}
nums = {'A':"ace", '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':"jack", 'Q':"queen", 'K':'king'}
print(f'{nums[num]} of {suits[suit.upper()]}')
