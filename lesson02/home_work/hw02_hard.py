# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# вычислите и выведите y

equation = 'y = -12x + 11111140.2121'

x = 2.5

y = float(equation[4:equation.find("x")]) * x + float(equation[11:])

print(y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

date = str(input('Введите дату в формате: dd.mm.yyyy '))
list_date = date.split('.')
day = int(list_date[0])
month = int(list_date[1])
year = int(list_date[2])
long_month = [1, 3, 5, 7, 8, 10, 12]

if date.find(".") != 2 or date.find(".", 3) != 5 or len(date) != 10:
    print('Дата введена не корректно')
elif day < 1 or day > 31:
    print('День введен не корректно')
elif month < 1 or month > 12:
    print('Месяц введен не корректно')
elif year < 1 or year > 9999:
    print('Год введен не корректно')
elif month not in long_month and day > 30:
    print('День введен не корректно')
else:
    print('Дата введена корректно:', date)

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

N = int(input('Введите номер комнаты:'))

floor = 1
room = 1
answer_floor = 0
answer_room = 0

if N <= 0 or N > 2000000000:
    print(f'Комнаты с номером {N} нет в нашем отеле. Возможно, вы ошиблись?')
else:
    while 1 <= N <= 2000000000:
        for current_floor in range(floor):
            answer_floor += 1
            for current_room in range(room):
                N -= 1
                if N == 0:
                    answer_room = current_room + 1
                    break
            if N == 0:
                break
        floor += 1
        room += 1
    if answer_floor == 1:
        print(f'Комната расположена на {answer_floor} этаже. Это единственная комната на этаже. Не заблудитесь.')
    else:
        print(f'Комната расположена на {answer_floor} этаже, {answer_room}-я слева.')
        
