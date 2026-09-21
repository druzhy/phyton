#Задача
#Дана строка, состоящая из слов, разделенных пробелами. Напишите программу, которая подсчитывает, сколько раз каждое слово встречается в тексте, и формирует из этого словарь.
#Приведите слова к нижнему регистру перед подсчетом.
#Входные данные
#Одна строка с текстом.
#Выходные данные
#Слово в нижнем регистре: количество их повторений.
#apple banan Apple baNan kiwi
words  = input().lower().split()
#print(words)
words_count = {}
for word in words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
#print(words_count)
for key , value in words_count.items():
    print(f"{key}: {value}")