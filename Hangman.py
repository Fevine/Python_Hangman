from random import choice

Animals = [
    'fox', 'cat', 'chicken', 'dog', 'tiger', 'cheetah', 'leopard',
    'crocodile', 'zebra', 'goat', 'sheep', 'rabbit', 'deer', 'elephant',
    'rhino', 'hummingbird', 'wolf', 'camel', 'shark', 'peacock', 'lion', 'griffe',
    'Whale', 'snake', 'panda', 'koala'
]


# Functions

def update (a):
    global Target, Hidden, Result
    a = a.lower()
    for i in range(int(len(Target))):
        if a == Target[i]:
            Hidden[i]=a
        Result = ''.join(Hidden)
    return Result




Target = choice(Animals)
Hidden = list(len(Target)*'_')
Result = ''.join(Hidden)

# Variables

Life = 6

print('Find the hidden animal')

Try = input('Try to find: ')

while Life > 0 and Result != Target:
    if Try != Target:
        if Try in Target:
            print('You found a letter')
            print(update(Try),'\n')
            if Result == Target:
                print('You won!')
                break
        else:
            print(f'{Try} is not in the word\n')
            print(Result,'\n')
            Life -=1
            print(f'Remaining Life {Life}')
            if Life == 0:
                print('You lose!')
                print(f'The animal was {Target}')
                break
        Try = input('Try to find: ')
    else:
        print('\nYou won!')
        break

