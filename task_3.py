'''

Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369

'''

num = int(input('Введите число '))
total = int(str(num)) + int(str(num) + str(num)) + int((str(num) + str(num) + str(num)))
print(f"Сумма чисел n + nn + nnn = {total}")
