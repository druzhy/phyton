# Задание
# Дан произвольный текст.
# Найдите слово, которое встречается в нём чаще всего.
# Если таких слов несколько, выведите первое по алфавиту. Регистр букв не учитывается.
# Входные данные
# Произвольный текст в одну строку.
# Выходные данные
# Одно слово в нижнем регистре, встречающееся чаще всего.
import re
text = input() #"Яблоко, груша, яблоко! Банан, груша... Яблоко и банан."
template = r'[^\w\s]' #шаблон, по которому выбираем не буквы и не цифры и не пробельные символы
#print(re.findall(template, text))
#print(re.sub(template,'',text.lower()))
words = re.sub(template,'',text.lower()).split() #заменяем найденные символы в строке на пусто
#print(words)
#запишем в словарь с подсчетом кол-ва
words_dict = {}
for word in words:
    if word in words_dict:
        words_dict[word] +=1
    else:
        words_dict[word] = 1
#print(words_dict)

#найдем максимальное значение
max_cnt = max(words_dict.values())
#print (max_cnt)

#вывод с сортировкой словаря
for word, cnt in sorted(words_dict.items()):
    if cnt == max_cnt:
        print(f"{word}")
        exit()