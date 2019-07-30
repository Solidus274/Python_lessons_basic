#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random

card_player = random.sample(range(90), 16)
card_machine = random.sample(range(90), 16)
5
print(card_player, card_machine)
barrel_bag = [i for i in range(91)]

row_a = card_player[:5] + [" "] * 4
row_b = card_player[5:10] + [" "] * 4
row_c = card_player[11:] + [" "] * 4
row_m_a = card_machine[:5] + [" "] * 4
row_m_b = card_machine[5:10] + [" "] * 4
row_m_c = card_machine[11:] + [" "] * 4

print("--------------------------")
print(*sorted(row_a, key=lambda x: random.random()))
print(*sorted(row_b, key=lambda x: random.random()))
print(*sorted(row_c, key=lambda x: random.random()))
print("--------------------------")
print()
print("--------------------------")
print(*sorted(row_m_a, key=lambda x: random.random()))
print(*sorted(row_m_b, key=lambda x: random.random()))
print(*sorted(row_m_c, key=lambda x: random.random()))
print("--------------------------")


def new_barrel(val):
   while len(val) > 0:
       x = random.choice(val)
       y = x
       val.remove(x)
       yield y


def barrel_choice(current_barrel):
    if card_player.count(current_barrel) > 0:
        print(f"Бинго! Цифра {current_barrel} есть в карточке игрока!")
        card_player.remove(current_barrel)
    else:
        print(f"Нифига. Цифры {current_barrel} нет в карточке игрока!")

    if card_machine.count(current_barrel) > 0:
        print(f"Бинго! Цифра {current_barrel} есть в карточке машины!")
        card_machine.remove(current_barrel)
    else:
        print(f"Нифига. Цифры {current_barrel} нет в карточке машины!")

barrel_iter = new_barrel(barrel_bag)

barrel_choice(next(barrel_iter))

print(card_player, card_machine)
