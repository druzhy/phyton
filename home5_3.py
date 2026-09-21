# Задание
# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.
#
# По окончанию рабочей недели имеем файл sold.txt.
# Товары проданные в один день аппарат записывает на одной строке.
#
# Узнайте:
#
# На какую сумму было продано всего товаров
# Цену самого дорогого товара
# Цену самого дешевого товара
# Формат входных данных
# Дан текстовый файл. На каждой строке записаны числа(целые или десятичные) разделенные одним или более пробелами.
#
# Количество строк в файле произвольное.
#
# Формат выходных данных
# Вывести три числа, каждое на отдельной строке, с точностью два знака:
#
# На какую сумму было продано товаров
# Цену самого дорогого товара
# Цену самого дешевого товара

with open("sold.txt","r", encoding="utf-8") as file:
    list_prices = []
    for line in file:
        #print(line.strip())
        list_prices.append(line.strip().split())
        #print(list_prices)
    #print(list_prices)

    list_prices_itog = []
    for list in list_prices:
        for price in list:
            list_prices_itog.append(float(price))
    #print(list_prices_itog)

    summa = 0
    for price in list_prices_itog:
         summa += price

    max_price = max(list_prices_itog)
    min_price = min(list_prices_itog)

    print(f"{summa:.2f}")
    print(f"{max_price:.2f}")
    print(f"{min_price:.2f}")
