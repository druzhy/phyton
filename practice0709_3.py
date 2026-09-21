#Задача
#Даны результаты голосования. С клавиатуры вводится количество записей N,
# а затем N строк, каждая из которых содержит имя кандидата и количество отданных за него голосов (через пробел).
#Напишите программу, которая считывает эти данные в словарь, определяет кандидата с наибольшим количеством голосов
# и выводит его имя и набранные баллы. Если победителей несколько, выведите любого из них.
#Входные данные
#В первой строке — целое число N (N≥1).
#В следующих N  строках — имя кандидата (одно слово) и целое число голосов, разделенные пробелом.
#Выходные данные
#Имя победителя и количество голосов через пробел.
n = int(input())
candidates = {}
for i in range(n):
    name, cnt_voice = input().split()
    if name in candidates:
        candidates[name] += int(cnt_voice)
    else:
        candidates[name] = int(cnt_voice)
#print(candidates)

#for name , cnt_voice in candidates.items():
#    print(f"{name}: {cnt_voice}")

winner_voice = 0
for name, cnt_voice in candidates.items():
    if  int(cnt_voice) > winner_voice:
        winner_voice = int(cnt_voice)
#print(winner_voice)

for name, cnt_voice in candidates.items():
    if int(cnt_voice) == winner_voice:
        print(f"{name} {cnt_voice}")
        exit()