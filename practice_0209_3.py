#Задание
#Дан список целых чисел и число, которое нужно удалить.
#Программа должна вывести список, в котором отсутствуют все вхождения заданного числа.
#Формат входных данных
#В первой строке вводится список целых чисел, через пробел.
#Во второй строке целое число (для удаления).
#Формат выходных данных
#Вывести оставшиеся после удаления числа, в одну строку через пробел.
numbers = list(map(int,input().split()))
n = int(input())
#numbers_copy = numbers
#for number in numbers_copy:
#    if number == n:
#       numbers.remove(number)
#print(*numbers)

#for number in numbers.copy():
#    if number == n:
#       numbers.remove(number)
#print(*numbers)

#for number in numbers[:]:
#    if number == n:
#       numbers.remove(number)
#print(*numbers)

while n in numbers:
    numbers.remove(n)
print(*numbers)