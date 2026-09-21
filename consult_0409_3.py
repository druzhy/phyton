#Задани
#Даны два списка целых чисел одинаковой длины.
#Создайте третий список, состоящий из сумм элементов исходных списков, стоящих на одинаковых позициях.
#Формат входных данных
#Даны две строки, каждая содержит целые числа, разделенные пробелами, элементы каждого списка введены на отдельной строке через пробел.
#Формат выходных данных
#Выведите список сумм парных элементов.
list_numbers1 = list(map(int,input().split()))
list_numbers2 = list(map(int,input().split()))
#list_summa = [ list_numbers1[i]+list_numbers2[i] for i in range(len(list_numbers1))]
#print(list_summa)

total = []
for el1, el2 in zip(list_numbers1, list_numbers2):
    total.append(el1 + el2)
print(total)