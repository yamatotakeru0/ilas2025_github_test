import random

guess = int(input('guess='))
print('Your guess is', guess)
answer = random.randint(1, 100)
if guess == answer :
    print('Good guess')
else:
    if (guess < answer):
        print('Too low')
    else:
        print('Too high')