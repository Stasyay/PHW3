#     Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#     Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = [1.1, 1.2, 3.1, 0, 10.01]
new_lst = []

for el in range(len(lst)):
    new_lst.append(lst[el]%1)
print(max(new_lst) - min(new_lst))