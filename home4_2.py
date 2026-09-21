# Задание
# Сначала подаётся число N — количество записей в справочнике.
# В следующих N строках вводятся имя и номер телефона через пробел.
# Затем вводится имя контакта, номер которого нужно найти.
# Гарантирует, что имена контаков уникальные(не повторяются).
# Входные данные
# В первой строке — целое число N
# В следующих N строках — пары Имя Номер.
# В последней строке — имя для поиска.
# Выходные данные
# Номер телефона найденного контакта или сообщение «Контакты не найдены», если такого имени нет.
n  = int(input())
contact_dict = {}
for i in range(n):
    name, phone = input().split()
    contact_dict[name] = phone
#print(contact_dict)

contact_for_search = input()

for name, phone in contact_dict.items():
    if name ==  contact_for_search:
        print(f"{phone}")

if contact_for_search not in contact_dict:
    print("Контакты не найдены")