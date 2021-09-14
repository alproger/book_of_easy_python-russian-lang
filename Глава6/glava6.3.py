guess_me = 5
number = (range(10))
for i in number:
    if i < guess_me :
        print('too low')
    elif i == guess_me :
        print('found it')
        break
    else:
        print('oops')