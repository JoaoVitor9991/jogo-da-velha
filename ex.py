from random import randrange


def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|  {0:^3}  |  {1:^3}  |  {2:^3}  |".format(row[0], row[1], row[2]))
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    valid = False
    while not valid:
        move = input("Digite seu movimento: ")
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move)
            row, col = divmod(move-1, 3)
            if board[row][col] not in ['X', 'O']:
                board[row][col] = 'O'
                valid = True
            else:
                print("Campo já ocupado! Tente outro.")
        else:
            print("Entrada inválida. Digite um número entre 1 e 9.")


def make_list_of_free_fields(board):
    free = [(r, c) for r in range(3) for c in range(3) if board[r][c] not in ['X', 'O']]
    return free


def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        row, col = free[randrange(len(free))]
        board[row][col] = 'X'


def victory_for(board, sign):
    win_cond = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    if [sign] * 3 in win_cond:
        return True
    return False


board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]


while True:
    display_board(board)
    enter_move(board)
    if victory_for(board, 'O'):
        display_board(board)
        print("Você ganhou!")
        break
    draw_move(board)
    if victory_for(board, 'X'):
        display_board(board)
        print("O computador ganhou!")
        break
    if not make_list_of_free_fields(board):
        display_board(board)
        print("Empate!")
        break