import random
answer = random.randint(1, 100)
#print("answer is" , answer)
guess = int(input('guess='))
print('Your guess is', guess)
truth = 0
while truth == 0 :
    if guess == answer :
        print('Good guess')
        truth = 1
    else :
        guess = int(input('guess='))
        print('Your guess is', guess)