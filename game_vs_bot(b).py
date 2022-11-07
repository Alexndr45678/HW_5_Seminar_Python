# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint

def move(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмёте (от 1 до 28): "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, ВВЕДИТЕ ЧИСЛО ОТ 1 до 28!: "))
    return x

def move_output(name, k, counter, value):
    print(f"Ходил/а {name}, взял/а {k} конфет, теперь у него/неё {counter} конфет. Всего осталось {value}.")

def bot_move(value):
    k = randint(1, 29)
    while value - k <= 28 and value > 29:
        k = randint(1, 29)
    return k

player1 = input("Введите своё имя: ")
player2 = "Mr. Bot"
value = 2021
selection = randint(0, 2)
counter1 = 0
counter2 = 0
    
if selection:
    print(f"Первый ходит {player1}")
else:
    print(f"Второй ходит {player2}")


while value > 28:
    if selection:
        k = move(player1)
        counter1 += k
        value -= k
        selection = False
        move_output(player1, k, counter1, value)
    else:
        k = bot_move(value)
        counter2 += k
        value -= k
        selection = True
        move_output(player2, k, counter2, value)

if selection:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")