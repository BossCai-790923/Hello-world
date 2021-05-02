
def Tic_tak_toe(coordinates1, coordinates2, turn):
    l = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
    ]
    while True:
        coordinates2 = int(input('Please input the X coordinates:'))
        coordinates1 = int(input('Please input the Y coordinates:'))
        # l='- - -' \
        #   '- - -' \
        #   '- - -'

        if turn == 1:
            print(f"Player {turn}'s turn")
            while True:
                if l[coordinates1][coordinates2]=='-':
                    l[coordinates1][coordinates2] = 'Y'
                    break
                else:
                    print('it is invalid.')
                    coordinates2 = int(input('Please input the X coordinates:'))
                    coordinates1 = int(input('Please input the Y coordinates:'))


            print(l[0])
            print(l[1])
            print(l[2])
        if turn == 2:
            print(f"Player {turn}'s turn")
            while True:
                if l[coordinates1][coordinates2]=='-':
                    l[coordinates1][coordinates2] = 'X'
                    break
                else:
                    print('it is invalid.')
                    coordinates2 = int(input('Please input the X coordinates:'))
                    coordinates1 = int(input('Please input the Y coordinates:'))
            print(l[0])
            print(l[1])
            print(l[2])
        # Win check
        win1 = False
        win2 = False
        n = 0
        # slide
        if l[n][n] == 'Y' and l[n + 1][n + 1] == 'Y' and l[n + 2][n + 2] == 'Y':
            win1 = True
        if l[n - 1][n - 1] == 'Y' and l[n - 2][n - 2] == 'Y' and l[n - 3][n - 3] == 'Y':
            win1 = True
        # Horizontal
        if l[0][0] == 'Y' and l[0][1] == 'Y' and l[0][2] == 'Y':
            win1 = True
        if l[1][0] == 'Y' and l[1][1] == 'Y' and l[1][2] == 'Y':
            win1 = True
        if l[2][0] == 'Y' and l[2][1] == 'Y' and l[2][2] == 'Y':
            win1 = True
        # Streight
        if l[0][0] == 'Y' and l[1][0] == 'Y' and l[2][0] == 'Y':
            win1 = True
        if l[0][1] == 'Y' and l[1][1] == 'Y' and l[2][1] == 'Y':
            win1 = True
        if l[0][2] == 'Y' and l[1][2] == 'Y' and l[2][2] == 'Y':
            win1 = True
        times=0
        n = 0
        # slide
        if l[n][n] == 'X' and l[n + 1][n + 1] == 'X' and l[n + 2][n + 2] == 'X':
            win2 = True
        if l[n - 1][n - 1] == 'X' and l[n - 2][n - 2] == 'X' and l[n - 3][n - 3] == 'X':
            win2 = True
        # Horizontal
        if l[0][0] == 'X' and l[0][1] == 'X' and l[0][2] == 'X':
            win2 = True
        if l[1][0] == 'X' and l[1][1] == 'X' and l[1][2] == 'X':
            win2 = True
        if l[2][0] == 'X' and l[2][1] == 'X' and l[2][2] == 'X':
            win2 = True
        # Streight
        if l[0][0] == 'X' and l[1][0] == 'X' and l[2][0] == 'X':
            win2 = True
        if l[0][1] == 'X' and l[1][1] == 'X' and l[2][1] == 'X':
            win2 = True
        if l[0][2] == 'X' and l[1][2] == 'X' and l[2][2] == 'X':
            win2 = True

        if win1:

            print('\n player 01 wins')
            l = [
                ['-', '-', '-'],
                ['-', '-', '-'],
                ['-', '-', '-']
            ]
        if win2:

            print('\n player O2 wins')
            l = [
                ['-', '-', '-'],
                ['-', '-', '-'],
                ['-', '-', '-']
            ]
        for i in range(3):
            for j in range(3):
                if l[i]!='-' and l[j]!='-':
                    times+=1
                    if times==9:
                        print('nobody wins')

        turn+=1

        if turn==3:
            turn=1



turn1=1
print('Tic tak toe game start ')
print('-' * len('Tic tak toe game start '))
print('generate list')
print('平局请手动判断:)')


Tic_tak_toe(0,0,1)
