# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32



result = 0
for i in range (3) :
    class1 = int(input("Ведите количество парт: "))
    if class1%2 == 0:
        result += class1/2
    else:
        result += class1//2 + 1
print ("Количество парт: ", result)

