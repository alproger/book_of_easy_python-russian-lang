guess_me, number  = 7, 1
while number <= guess_me:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
    number += 1