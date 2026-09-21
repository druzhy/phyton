# Задание
# Вам дан список пар слов-синонимов. После списка даётся одно слово, для которого нужно найти синоним.
# Входные данные
# В первой строке — целое число N
# В следующих N строках — пары синонимов через пробел.
# В последней строке — одно слово.
# Гарантируется, что последнее слово присутсвует среди слов синонимов.
# Выходные данные
# Слово-синоним для запрашиваемого слова. Поиск работает в обе стороны (по первому слову можно найти второе, и наоборот).
n  = int(input())
sinonim_dict = {}
for i in range(n):
    word, sinonim = input().split()
    sinonim_dict[word] = sinonim
#print(sinonim_dict)

word_for_search = input()

for word, sinonim in sinonim_dict.items():
    if sinonim ==  word_for_search:
        print(f"{word}")
    if word == word_for_search:
        print(f"{sinonim}")

