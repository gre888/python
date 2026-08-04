for x in range(1, 6):
    for y in range(1, 6 - x):
        print(' ', end='')
    for y in range(1, x + 1):
        print('*', end = '')
    print ( )  #換到下一行
print ( )  #最後空白行