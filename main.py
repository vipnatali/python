# Напишите программу, которая на вход принимает два числа и проверяет
# является ли одно число квадратом другого.
# 5, 25 -> да
# 4,16 -> да
# 8, 9 -> нет


a = int(input ())
b = int(input ())
if a**2 == b or b**2 == a:
    print('да')
else:
    print('нет')
    