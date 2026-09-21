# Задание
# В соцсетях пользователи отмечают темы с помощью хештегов, которые начинаются со символа # и состоят из букв и цифр.
# Извлеките из текста все хештеги.
# Входные данные
# Одна строка текста, содержащая слова и хештеги (например, #python, #code2026).
# В исходной строке знаки препинания отсутствуют.
# Выходные данные
# Все найденные хештеги в порядке их появления в тексте, каждый с новой строки.
import re
words_list = list(input().split())
for word in words_list:
    if word[0] == "#":
         print(word)

# text  = input() #re.escape(input())
# print(text)
# template = r'\b#\w+'
# result  = re.findall(template, text)
# print(result)

#for word in result:
#    print(word)