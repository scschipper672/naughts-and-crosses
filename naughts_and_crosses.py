
players = ['o', 'x']
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def make_board_string(board):
    return f'    1   2   3\n\
  a {board[0][0]} | {board[0][1]} | {board[0][2]}\n\
   ---+---+---\n\
  b {board[1][0]} | {board[1][1]} | {board[1][2]}\n\
   ---+---+---\n\
  c {board[2][0]} | {board[2][1]} | {board[2][2]}'

def change_turn():
    change = players.pop(0)
    players.append(change)
    return players[0]

def win(player):
    return [player, player, player] in board or (
            board[0][0] == board[1][0] == board[2][0] == player) or (
            board[0][1] == board[1][1] == board[2][1] == player) or (
            board[0][2] == board[1][2] == board[2][2] == player) or (
            board[0][0] == board[1][1] == board[2][2] == player) or (
            board[0][2] == board[1][1] == board[2][0] == player)

def get_move(turn):
    my_move = input(f"{turn}'s move: ")
    if not (len(my_move) == 2 and my_move[0] in 'abc' and my_move[1] in '123'):
        print(f'\n{turn}, type the coordinates for your move')
        print('Eg) a1')
        return get_move(turn)
    return {'x': 'abc'.find(my_move[0]),
            'y': '123'.find(my_move[1])}

def make_move(turn, board):
    my_move = get_move(turn)
    if board[int(my_move['x'])][int(my_move['y'])] != ' ':
        print('abc'[my_move['x']] + '123'[my_move['y']] + ' is already taken!')
        return make_move(turn, board)
    board[int(my_move['x'])][int(my_move['y'])] = turn
    return board

while True:
    turn = change_turn()

    print(f"{make_board_string(board)}\n")
    if ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]:
        print(' ---- Draw ----')
        break

    board = make_move(turn, board)

    if win(turn):
        print(f'CONGRATULATIONS {turn.upper()}!! YOU WIN')
        break

    print('\n'*100) # Scroll the previous board out of view
