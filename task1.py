# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

# Пример:
#     [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

lst = [2, 100, 2, -9, 98]
sum = 0

for i in range(len(lst)):
    if i%2 !=0:
        sum += lst[i] 
print (lst)
print (f'сумма чисел на нечетных индексах =  {sum}')
