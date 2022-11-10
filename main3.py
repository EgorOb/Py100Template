# field = [[],[],[]]
def draw_field(field):
    for row in field:
        for cell in row:
            print(f"|{cell}", end="")
        print("|")


def is_win(field):
    return False


def check_int_val(text ,max_val=None):
    """Проверили число"""
    while True:
        val = input(text)
        if not val.isdigit():
            print("Не число, введи число")
            continue
        else:
            val = int(val)
            if max_val is not None and not 0 <= val <= max_val:
                print(f"Вышел за рамки [0, {max_val}]")
                continue
        return val


def check_player_in_field(field):
    while True:
        ind_row = check_int_val("Введи номер строки\n", max_val=3)
        ind_col = check_int_val("Введи номер столбца\n", max_val=3)
        if field[ind_row][ind_col] != " ":
            print("Ячейка занята")
            continue
        return ind_row, ind_col


def game(field, player, size):
    count = 0
    draw_field(field)
    while count < size*size:
        ind_row, ind_col = check_player_in_field(field)
        field[ind_row][ind_col] = player
        draw_field(field)
        count += 1
        if is_win(field):
            print(f"Выиграл {player}")
            return player
        player = "X" if player == "0" else "0"
    print("Ничья")


def app():
    size = 3
    player = "X"
    field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    game(field, player, size)


if __name__ == "__main__":
    app()

              
                
# def loop(func, *args):
#     while True:
#         vars = func(*args)
#         if vars:
#             return vars

# def check_player_in_field1(field):
#     ind_row = check_int_val("Введи номер строки", max_val=3)
#     ind_col = check_int_val("Введи номер столбца", max_val=3)
#     if field[ind_row][ind_col] != "":
#         print("Ячейка занята")
#         return False
#     return ind_row, ind_col

# vars = loop(check_player_in_field1, field)