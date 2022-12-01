#     Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

#     Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(k):
    if k == 0: return 0
    elif k ==1: return 1
    return (fib(k-1) + fib(k-2))

def negafib(k):
    if k == 0: return 0
    elif k ==-1: return 1
    return (negafib(k+2) - negafib(k+1))

k = int(input("введите число: "))
lst_fib = []
lst_negafib = []
for el in range(-k, k+1):
    if el >= 0:
        lst_fib.append(fib(el))
    elif el < 0:
        lst_negafib.append(negafib(el))
  
print(lst_negafib + lst_fib)  
