#Задание
#Дана строка, состоящая из слов, разделенных пробелами.
#Сформируйте список, содержащий длины каждого из слов в строке, и выведите его на экран.
#Формат входных данных
#Дана одна строка.
#Формат выходных данных
#Выведите итоговый список длин слов.
list_input = input().split()
#list_len = []
#for i in list_input:
#    list_len.append(len(i))
#print(list_len)
list_len = [len(word) for word in list_input ]
print(list_len)