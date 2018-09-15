
player = ['o', 'x']

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def make_board_string(board):
    return f'    1   2   3\n\
  a {board[0][0]} | {board[0][1]} | {board[0][2]}\n\
   ---+---+---\n\
  b {board[1][0]} | {board[1][1]} | {board[1][2]}\n\
   ---+---+---\n\
  c {board[2][0]} | {board[2][1]} | {board[2][2]}'

def change_turn():
    change = player.pop(0)
    player.append(change)
    return player[0]

def win(player):
    return [player, player, player] in board or (
            board[0][0] == player and board[1][0] == player and board[2][0] == player) or (
            board[0][1] == player and board[1][1] == player and board[2][1] == player) or (
            board[0][2] == player and board[1][2] == player and board[2][2] == player) or (
            board[0][0] == player and board[1][1] == player and board[2][2] == player) or (
            board[0][2] == player and board[1][1] == player and board[2][0] == player)

while True:
    turn = change_turn()

    print(f"{make_board_string(board)}\n")
    my_move = input(f"{turn}'s move: ")

    while not (len(my_move) == 2 and my_move[0] in 'abc' and my_move[1] in '123'):
        print(f'\n{turn}, type the coordinates for your move')
        print('Eg) a1')
        my_move = input(f"{turn}'s move: ")

    # make the move
    move_x = 'abc'.find(my_move[0])
    move_y = '123'.find(my_move[1])
    board[int(move_x)][int(move_y)] = turn
   # print(f'{move_x}, {move_y}')
    #print(f'{board[int(move_x)][int(move_y)]}')
    #print(f"{board_string}\n")

    if ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]:
        print('----- Draw -----')
        break
    if win(turn):
        print(f'CONGRATULATIONS {turn.upper()}!! YOU WIN')
        break
