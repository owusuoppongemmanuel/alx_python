for i in range(100):
    if(i / 10 != i % 10) and (i / 10 < i % 10):
        if(i < 89):
            print('{:02d}, '.format(i), end='')
        else :
            print('{:02d}'.format(i))