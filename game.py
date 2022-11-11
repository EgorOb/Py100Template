from typing import List

# def create_field(size: int, empty_cell: str) -> List[List]:


def create_field(size: int, empty_cell: str) -> list[list]:
    """
    Создание двумерного поля
    :param size: размер поля
    :return: 
    """
    tmp = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(empty_cell)
        tmp.append(row)
    return tmp

def create_field_short(size, empty_cell):
    """
    Создание двумерного поля
    :param size: размер поля
    :return: 
    """
    tmp = []
    for i in range(size):
        tmp.append([empty_cell]*size)
    return tmp


def main():
    size = check_int_val("Введите размер поля\n") # задали поле (можно из консоли input())
    field = create_field_short(size, " ")
    player = "X" # выбор игрока (можно из консоли input())
    change = 1
    if change == 1:
        game(field, player, size)
    else:
        print("В разработке")

def game(field, player, size):
    current_player = player
    count_step = 0 # счетчик ходов
    draw_field(field) # нарисовали поле
    
    while count_step < size*size:
        # необходимо постать игрока на поле
        i_row, i_col = get_index_in_field(field, size-1, current_player) # получаем индексы куда будет ставить игрок
        field = set_player_in_field(field, current_player, i_row, i_col) # ставит игрока
        count_step += 1 # обновили счетчик ходов
        draw_field(field)  # перерисовали поле
        if is_win(field):
            print(f"Выиграл игрок {current_player}")
            return current_player
        current_player = change_player(current_player) # сменили игрока
    
    # if count_step == size*size:
    #     print("Ничья")
    print("Ничья")
    return None
        
                
def draw_field(field):
    """
    Рисуем поле
    :param field: 
    :return: 
    """
    for row in field:
        for cell in row:
            print(f"|{cell}", end="")
        print("|")


def check_int_val(text, max_border=None):
    """
    Проверка что число целое, .....
    :return: 
    """
    while True:
        val = input(text)
        try:
            val = int(val)
        except ValueError:
            print("Должно быть число")
            continue
        if max_border is not None:
            if not 0 <= val <= max_border:
                print(f"Должно лежать от 0 до {max_border}")
                continue
        break
    return val
        


def check_in_field(field, size):
    """
    Провожу проверку, что можно поставить по индексу на поле
    :param field: 
    :return: 
    """
    while True:
        row = check_int_val("Введите номер строки\n", max_border=size)
        col = check_int_val("Введите номер колонки\n", max_border=size)
        if field[row][col] == " ":
            return row, col
        print("Ячекa занята!")


def get_index_in_field(field, size, current_player):
    print(f"Ставит игрок {current_player}")
    return check_in_field(field, size)


def set_player_in_field(field, player, i_row, i_col):
    field[i_row][i_col] = player
    return field


def is_win(field, win_var=None):
    """
    Возращает True если кто-то выиграл, если нет то False
    Если ничья, то False
    :param field: 
    :param win_var: 
    :return: 
    """
    # Проверки....
    # Кто-то выиграл return True
    return False


def get_win_var(size):
    """
    Возвращает список выигрыщных позиций
    :param size: 
    :return: 
    """
    pass
        
def get_cell(index, size):
    row, col = divmod(index - 1, size)
    return row, col

def change_player(player):
    """
    Алгоритм смены игрока
    :param player: текущий игрок
    :return: 
    """
    player_new = "X" if player == "0" else "0"
    # if player == "0":
    #     player_new = "X"
    # else:
    #     player_new = "0"
    
    return player_new

if __name__ == "__main__":
    main()