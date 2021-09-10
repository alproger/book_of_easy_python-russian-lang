from random import randint
secret = randint(1, 10)
guess = randint(1, 10)
if guess < secret :
    print('too low')
elif guess > secret :
    print('to hight')
elif guess == secret:
    print('just right')


