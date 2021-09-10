from random import randint
small = bool(randint(0,1))
green = bool(randint(0,1))


if small and green == False:
    print('Вышня')

elif small and green:
    print('горошек')

elif small == False and green:
    print('арбуз')

else:
    print('Тыква')

