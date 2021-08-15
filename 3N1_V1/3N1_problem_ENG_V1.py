
while True:
    calcolatore = 0

    x = int(input('insert a positive entire number\n'))

    while x != 4:

        if x %2 ==0:
            x = x /2
            calcolatore = calcolatore + 1
            print(x)
        else:
            x = x *3+1
            calcolatore = calcolatore + 1
            print(x)
    else:
        print('\nThat\'s a loop!!')
        print('step needed for the loop ' + str(calcolatore))
