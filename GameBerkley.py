from random import randrange
from tkinter import *


def check_win_field(row, col, field, ctb):
    global field_of_field
    for i in range(3):
        if field[i][0]['text'] == field[i][1]['text'] == field[i][2]['text'] == ctb:
            field[i][0]['background'] = field[i][1]['background'] = field[i][2]['background'] = 'pink'
            field_of_field[row][col] = ctb
            return True
        if field[0][i]['text'] == field[1][i]['text'] == field[2][i]['text'] == ctb:
            field[0][i]['background'] = field[1][i]['background'] = field[2][i]['background'] = 'pink'
            field_of_field[row][col] = ctb
            return True
        if field[0][0]['text'] == field[1][1]['text'] == field[2][2]['text'] == ctb:
            field[0][0]['background'] = field[1][1]['background'] = field[2][2]['background'] = 'pink'
            field_of_field[row][col] = ctb
            return True
        if field[2][0]['text'] == field[1][1]['text'] == field[0][2]['text'] == ctb:
            field[2][0]['background'] = field[1][1]['background'] = field[0][2]['background'] = 'pink'
            field_of_field[row][col] = ctb
            return True
    else:
        return False


def check_win_game(field, ctb):
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] == ctb:
            return True
        if field[0][i] == field[1][i] == field[2][i] == ctb:
            return True
        if field[0][0] == field[1][1] == field[2][2] == ctb or field[2][0] == field[1][1] == field[0][2] == ctb:
            return True
    else:
        return False


def win(cmd):
    if cmd == 'O':
        Label(game, text='Вы проиграли.', font=("Arial", 30)).grid(row=0, column=0, columnspan=9, rowspan=9)
    else:
        Label(game, text='Вы выиграли.', font=("Arial", 30)).grid(row=0, column=0, columnspan=9, rowspan=9)


def can_win_or_loss(field, cmd):
    for i in range(3):
        if field[0][i]['text'] == field[1][i]['text'] == cmd and field[2][i]['text'] == ' ':
            field[2][i]['text'] = 'O'
            return 2, i
        if field[1][i]['text'] == field[2][i]['text'] == cmd and field[0][i]['text'] == ' ':
            field[0][i]['text'] = 'O'
            return 0, i
        if field[0][i]['text'] == field[2][i]['text'] == cmd and field[1][i]['text'] == ' ':
            field[1][i]['text'] = 'O'
            return 1, i
        if field[i][0]['text'] == field[i][1]['text'] == cmd and field[i][2]['text'] == ' ':
            field[i][2]['text'] = 'O'
            return i, 2
        if field[i][1]['text'] == field[i][2]['text'] == cmd and field[i][0]['text'] == ' ':
            field[i][0]['text'] = 'O'
            return i, 0
        if field[i][0]['text'] == field[i][2]['text'] == cmd and field[i][1]['text'] == ' ':
            field[i][1]['text'] = 'O'
            return i, 1
    if field[0][0]['text'] == field[2][2]['text'] == cmd and field[1][1]['text'] == ' ':
            field[1][1]['text'] = 'O'
            return 1, 1
    if field[1][1]['text'] == field[2][2]['text'] == cmd and field[0][0]['text'] == ' ':
            field[0][0]['text'] = 'O'
            return 0, 0
    if field[0][0]['text'] == field[1][1]['text'] == cmd and field[2][2]['text'] == ' ':
            field[2][2]['text'] = 'O'
            return 2, 2
    if field[2][0]['text'] == field[1][1]['text'] == cmd and field[0][2]['text'] == ' ':
            field[0][2]['text'] = 'O'
            return 0, 2
    if field[2][0]['text'] == field[0][2]['text'] == cmd and field[1][1]['text'] == ' ':
            field[1][1]['text'] = 'O'
            return 1, 1
    if field[1][1]['text'] == field[0][2]['text'] == cmd and field[2][0]['text'] == ' ':
            field[2][0]['text'] = 'O'
            return 2, 0
    return -1, -1


def check_full_field(field):
    for row in range(3):
        for col in range(3):
            if field[row][col]['text'] == ' ':
                return False
    return True


def move_computer():
    global now_field, color
    if check_full_field(now_field):
        standoff()
    row, col = can_win_or_loss(now_field, 'O')
    if row != -1:
        if check_win_field(now_row, now_col, now_field, 'O') and check_win_game(field_of_field, 'O'):
            win('O')
        now_field = field[row][col]
        color = now_field[0][0]['background']
        color_field(now_field)
        return
    row, col = can_win_or_loss(now_field, 'X')
    if row != -1:
        now_field = field[row][col]
        color = now_field[0][0]['background']
        color_field(now_field)
        return
    while True:
        row, col = randrange(3), randrange(3)
        if field_of_field[row][col] == -1 and now_field[row][col]['text'] == ' ':
            now_field[row][col]['text'] = 'O'
            now_field = field[row][col]
            color = now_field[0][0]['background']
            color_field(now_field)
            break


def click(row_mass, col_mass, row, col):
    global now_field, now_row, now_col, color
    if check_full_field(now_field):
        standoff()
    if now_field[row][col]['text'] == ' ' and now_field[row][col] == field[row_mass][col_mass][row][col]:
        color_field(now_field, color)
        now_field[row][col]['text'] = 'X'
        if check_win_field(row_mass, col_mass, now_field, 'X'):
            if check_win_game(field_of_field, 'X'):
                win('X')
        now_field, now_row, now_col = field[row][col], row, col
        move_computer()


def standoff():
    Label(game, text='Ничья.', font=("Arial", 30)).grid(row=0, column=0, columnspan=9, rowspan=9)


def new_game():
    global color, now_col, now_row, now_field
    for row_mass in range(3):
        for col_mass in range(3):
            for row in range(3):
                for col in range(3):
                    button = Button(game, text=' ', width=2, height=1,
                                    font=('Verdana', 20, 'bold'),
                                    background=list_colors[row_mass * 3 + col_mass],
                                    command=lambda row_mass=row_mass, row=row, col_mass=col_mass, col=col: click(
                                        row_mass, col_mass, row, col))
                    button.grid(row=row_mass * 3 + row, column=col_mass * 3 + col, sticky='nsew')
                    field[row_mass][col_mass][row][col] = button
    now_row, now_col = randrange(3), randrange(3)
    now_field = field[now_row][now_col]
    color = now_field[0][0]['background']
    color_field(now_field)


def color_field(field, color='white'):
    for i in range(3):
        for j in range(3):
            field[i][j]['background'] = color


game = Tk()
game.title('Крестики-нолики Беркли')

field_of_field = [[-1 for _ in range(3)] for _ in range(3)]
list_colors = ['lemonchiffon', 'orange', 'grey', 'palegreen', 'royalblue', 'coral', 'violet', 'sandybrown', 'paleturquoise']
field = [[[[' ' for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)]

for row_mass in range(3):
    for col_mass in range(3):
        for row in range(3):
            for col in range(3):
                button = Button(game, text=' ', width=2, height=1,
                                            font=('Verdana', 20, 'bold'),
                                            background=list_colors[row_mass * 3 + col_mass],
                                            command=lambda row_mass=row_mass, row=row, col_mass=col_mass, col=col: click(row_mass, col_mass, row, col))
                button.grid(row=row_mass * 3 + row, column=col_mass * 3 + col, sticky='nsew')
                field[row_mass][col_mass][row][col] = button


new_button = Button(game, text='Новая игра', command=new_game)
new_button.grid(row=9, column=0, columnspan=9, sticky='nsew')
Label(game, text='Игра идёт на белом поле').grid(row=10, column=0, columnspan=9, sticky='nsew')

now_row, now_col = randrange(3),randrange(3)
now_field = field[now_row][now_col]
color = now_field[0][0]['background']
color_field(now_field)

game.mainloop()
