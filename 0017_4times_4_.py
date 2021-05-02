# import os
# def clear():
#     os.system('cls')

win_dc_1 = 'player 01 wins'
win_dc_2 = 'player 02 wins'
def Tic_tak_toe(coordinates1, coordinates2, turn):
    count_no=0
    l = [
    ['-', '-', '-','-'],
    ['-', '-', '-','-'],
    ['-', '-', '-','-'],
    ['-', '-', '-','-']
    ]
    while True:
        win1 = False
        win2 = False
        if count_no==17 and win1!=True and win2!=True:
            print('Nobody wins.')
            break
        coordinates2 = int(input('Please input the X coordinates(width):'))
        coordinates1 = int(input('Please input the Y coordinates(height):'))
        count_no+=1

        coordinates2-=1
        coordinates1-=1
        if turn == 1:
            print(f"Player {turn}'s turn")
            l[coordinates1][coordinates2] = 'O'
            print(' _1    2    3    4_')
            print(l[0])
            print(l[1])
            print(l[2])
            print(l[3])

        if turn == 2:
            print(f"Player {turn}'s turn")
            l[coordinates1][coordinates2] = 'X'
            print(' _1    2    3    4_')
            print(l[0])
            print(l[1])
            print(l[2])
            print(l[3])
        n = 0
        if l[n][n] == 'O' and l[n + 1][n + 1] == 'O' and l[n + 2][n + 2] == 'O' and l[n + 3][n + 3]:
            win1 = True
        if l[n - 1][n - 1] == 'O' and l[n - 2][n - 2] == 'O' and l[n - 3][n - 3] == 'O' and l[n - 4][n - 4] == 'O':
            win1 = True
        # Horizontal
        if l[0][0] == 'O' and l[0][1] == 'O' and l[0][2] == 'O' and l[0][3]=='O':
            win1 = True
        if l[1][0] == 'O' and l[1][1] == 'O' and l[1][2] == 'O' and l[1][3]=='O':
            win1 = True
        if l[2][0] == 'O' and l[2][1] == 'O' and l[2][2] == 'O' and l[2][3]=='O':
            win1 = True
        if l[3][0] == 'O' and l[3][1] == 'O' and l[3][2] == 'O' and l[3][3]=='O':
            win1 = True
        if l[0][0] == 'O' and l[1][0] == 'O' and l[2][0] == 'O' and l[3][0]=='O':
            win1 = True
        if l[0][1] == 'O' and l[1][1] == 'O' and l[2][1] == 'O' and l[3][1]=='O':
            win1 = True
        if l[0][2] == 'O' and l[1][2] == 'O' and l[2][2] == 'O' and l[3][2]=='O':
            win1 = True
        if l[0][3] == 'O' and l[1][3] == 'O' and l[2][3] == 'O' and l[3][3]=='O':
            win1 = True
        n = 0
        if l[n][n] == 'X' and l[n + 1][n + 1] == 'X' and l[n + 2][n + 2] == 'X' and l[n + 3][n + 3] == 'X' :
            win2 = True
        if l[n - 1][n - 1] == 'X' and l[n - 2][n - 2] == 'X' and l[n - 3][n - 3] == 'X' and l[n - 4][n - 4] == 'X':
            win2 = True
        if l[0][0] == 'X' and l[0][1] == 'X' and l[0][2] == 'X' and l[0][3]=='X':
            win1 = True
        if l[1][0] == 'X' and l[1][1] == 'X' and l[1][2] == 'X' and l[1][3]=='X':
            win1 = True
        if l[2][0] == 'X' and l[2][1] == 'X' and l[2][2] == 'X' and l[2][3]=='X':
            win1 = True
        if l[3][0] == 'X' and l[3][1] == 'X' and l[3][2] == 'X' and l[3][3]=='X':
            win1 = True
        if l[0][0] == 'X' and l[1][0] == 'X' and l[2][0] == 'X' and l[3][0]=='X':
            win1 = True
        if l[0][1] == 'X' and l[1][1] == 'X' and l[2][1] == 'X' and l[3][1]=='X':
            win1 = True
        if l[0][2] == 'X' and l[1][2] == 'X' and l[2][2] == 'X' and l[3][2]=='X':
            win1 = True
        if l[0][3] == 'X' and l[1][3] == 'X' and l[2][3] == 'X' and l[3][3]=='X':
            win1 = True
        if win1:
            print('\n'*20)
            print('\n',win_dc_1)
            l = [
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-']
            ]
            print('________New_game_started___________')
        if win2:
            print('\n'*20)
            print('\n',win_dc_2)
            l = [
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-']
            ]
            print('________New_game_started___________')
        turn+=1
        if turn==3:
            turn=1
turn1=1
print('Tic tak toe game start ')
print('-' * len('Tic tak toe game start '))
print('generate list')
print('Done')
Tic_tak_toe(0,0,1)
