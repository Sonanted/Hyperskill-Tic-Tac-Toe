def input_check(c):
    m = input('Enter the coordinates:').split()
    if not m[0].isdigit() or not m[1].isdigit():
        print('You should enter numbers!')
        return input_check(c)
    elif (int(m[0]) < 1 or int(m[0]) > 3) or (int(m[1]) < 1 or int(m[1]) > 3):
        print('Coordinates should be from 1 to 3!')
        return input_check(c)
    elif cells[int(m[0]) - 1 + 3 * (3 - int(m[1]))] != ' ':
        print('This cell is occupied! Choose another one!')
        return input_check(c)
    else:
        return m


def field(c):
    print('---------')
    print('|', cells[0], cells[1], cells[2], '|')
    print('|', cells[3], cells[4], cells[5], '|')
    print('|', cells[6], cells[7], cells[8], '|')
    print('---------')


def state_check(c):
    num_of_x = 0
    num_of_o = 0
    x_win = False
    o_win = False
    end = False
    if cells[0] == cells[1] == cells[2] == 'X' or cells[3] == cells[4] == cells[5] == 'X' or cells[6] == cells[7] == \
            cells[
                8] == 'X' or cells[0] == cells[3] == cells[6] == 'X' or cells[1] == cells[4] == cells[7] == 'X' or \
            cells[2] == \
            cells[5] == cells[8] == 'X' or cells[0] == cells[4] == cells[8] == 'X' or cells[2] == cells[4] == cells[
        6] == 'X':
        x_win = True
    if cells[0] == cells[1] == cells[2] == 'O' or cells[3] == cells[4] == cells[5] == 'O' or cells[6] == cells[7] == \
            cells[
                8] == 'O' or cells[0] == cells[3] == cells[6] == 'O' or cells[1] == cells[4] == cells[7] == 'O' or \
            cells[2] == \
            cells[5] == cells[8] == 'O' or cells[0] == cells[4] == cells[8] == 'O' or cells[2] == cells[4] == cells[
        6] == 'O':
        o_win = True
    for x in cells:
        if x == 'X':
            num_of_x += 1
        if x == 'O':
            num_of_o += 1
        if x == '_' or x == ' ':
            unfinished = True
    if x_win:
        print("X wins")
        end = True
    elif o_win:
        print("O wins")
        end = True
    if (num_of_o + num_of_x) == 9 and not o_win and not x_win:
        print("Draw")
        end = True
    return end


def move(c, ms):
    m = input_check(c)
    if ms % 2 != 0:
        c[int(m[0]) - 1 + 3 * (3 - int(m[1]))] = 'X'
    else:
        c[int(m[0]) - 1 + 3 * (3 - int(m[1]))] = 'O'


cells = list('         ')
moves = 0
while moves < 10:
    field(cells)
    game_statement = state_check(cells)
    if not game_statement:
        moves += 1
        move(cells, moves)
    else:
        break
