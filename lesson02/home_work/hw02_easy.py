# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

"""
Будем полагать, что 'яблоко' - самый длинный элемент в списке,
 а значит для форматирования нужно 6 отступов.
Иначе, пробегаемся по элементам массива и находим самый длинный
"""
fruits = ["яблоко", "банан", "киви", "арбуз"]
width = len('яблоко')
i = 0
while i < len(fruits):
    print('{0}. {1:>{width}}'.format(i, fruits[i], width=width))
    i += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# Пусть list1 и list2 - произвольные списки
list1 = ["a", "b", "c"]
list2 = ["d", "b", "c"]

"""
Пробегаемся по всему второму списку.
Если елемент второго списка присутствует в первом, 
  то произовдим удаление из первого списка по значению 
"""
for el in list2:
    if el in list1:
        list1.remove(el)



# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

# Определим список из произвольных целых чисел
list_old = [5, 67, 40, 22, 13, 6]

# Инициализируем новый список
list_new = []

"""
Пробегаемся по элементам списка.
Если элемент делится на 2 без остатка - делим его на 4 и добавляем в новый список.
Иначе - умножаем его на 2 и добаляем в новый список.
"""
for el in list_old:
    if el % 2 == 0:
        list_new.append(el/4)
    else:
        list_new.append(el * 2)

