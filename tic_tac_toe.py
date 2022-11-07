# Игра крестики нолики.

print("*" * 7, "Крестики-нолики", "*" * 7)

table = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def create_table(table):
    print("-" * 13)
    for i in range(3):
        print("|", table[0 + i * 3], "|", table[1 + i * 3], "|", table[2 + i * 3], "|")
        print("-" * 13)

def player_move(player_side):
    status = False
    while not status:
        cell_selection = input(f"Выберите ячейку для хода {player_side}: ")
        try:
            cell_selection = int(cell_selection)
        except:
            print("Введите НОМЕР ячейки от 1 до 9!")
            continue
        if cell_selection >= 1 and cell_selection <= 9:
            if (str(table[cell_selection - 1]) not in "XO"):
                table[cell_selection - 1] = player_side
                status = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9: ")

def check_win(table):
    win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_comb:
        if table[i[0]] == table[i[1]] == table[i[2]]:
            return table[i[0]]
    return False

def game(table):
    counter = 0
    win = False
    while not win:
        create_table(table)
        if counter % 2 == 0:
            player_move("X")
        else:
            player_move("O")
        counter += 1
        if counter > 4:
            tmp = check_win(table)
            if tmp:
                print(tmp, "поздравляем с победой!")
                win = True
                break
        if counter == 9:
            print("У нас ничья!")
            break
    create_table(table)

game(table)
print("Конец игры!")