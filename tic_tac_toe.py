import numpy

mat = numpy.array([
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
])
r = 0
c = 0


def board_tic():
    board = f'{mat[0, 0]}|{mat[0, 1]}|{mat[0, 2]}\n{mat[1, 0]}|{mat[1, 1]}|{mat[1, 2]}\n{mat[2, 0]}|{mat[2, 1]}|{mat[2, 2]}'
    print(board)


def bool_check_win():
    for i in range(3):
        if mat[i, 0] == mat[i, 1] == mat[i, 2] or mat[0, i] == mat[1, i] == mat[2, i]:
            return True
    if mat[0, 0] == mat[1, 1] == mat[2, 2] or mat[0, 2] == mat[1, 1] == mat[2, 1]:
        return True
    return False


def play_game():
    user = ['X', 'O']
    current_player = user[0]
    digit = 0

    while not bool_check_win():
        board_tic()
        digit = int(input(f'{current_player} enter: '))

        positions = {
            1: (0, 0), 2: (0, 1), 3: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            7: (2, 0), 8: (2, 1), 9: (2, 2)
        }

        if digit in positions.keys():
            row, col = positions[digit]
            if mat[row, col] != 'X' and mat[row, col] != 'O':
                mat[row, col] = current_player
                if bool_check_win():
                    print(f'{current_player} wins!!')
                    break
                elif current_player == user[0]:
                    current_player = user[1]
                else:
                    current_player = user[0]
            else:
                print('Position already filled,Try again!!')
        elif digit != -1 and not bool_check_win():
            print('Its draw!!')
            break


play_game()
