import random
print('---GUESSING GAME---')
n = (random.randint(0,10))
nu = int(input('Insert your guess: '))

if nu == n:
    print('Congrats, your guess is right!')
else:
    print('Your guess is wrong, the number was {}!'.format(n))
input('Press ENTER to exit')
