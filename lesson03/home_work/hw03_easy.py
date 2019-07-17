# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = str(number)
    number = number.split(".")
    if int(number[1][ndigits]) <= 4:
        number[1] = number[1][:ndigits]
    else:
        if int(number[1][0]) == 9:
            number[0] = str(int(number[0]) + 1)
            number[1] = str(int(number[1][:ndigits]) + 1)[1:]
        else:
            number[1] = str(int(number[1][:ndigits]) + 1)
    number = float(number[0] + "." + number[1])
    return number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket = str(ticket_number)
    tekcit = ticket[::-1]
    sum_1 = 0
    sum_2 = 0
    for x in range (int(len(ticket) / 2)):
        sum_1 += int(ticket[0 + x])
        sum_2 += int(tekcit[0 + x])
    if sum_1 == sum_2:
        return 'Счастливый'
    else:
        return 'Обычный'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
