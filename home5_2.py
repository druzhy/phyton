# Задание
# Формат входных данных
# Дан непустой текстовый файл. В каждой строке файла записано целое число.
#
# Формат выходных данных
# Вывести сумму всех чисел и среднеарифметическое этих чисел,
# на одной строке через пробел, с точностью до двух знаков.

with open("numbers.txt","r", encoding="utf-8") as file:
    list_numbers = []
    for line in file:
        #print(line.strip())
        list_numbers.append(int(line.strip()))
    #print(list_numbers)
    summa = 0
    for number in list_numbers:
        summa += number
    avg_numbers = summa / len(list_numbers)
    print(f"{summa} {avg_numbers:.2f}")