# Задача № 3, Д № 2. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму, округлённую до трёх знаков после точки.

# def new_list(N):
#     lst = []
#     i = 0
#     sum = 0
#     for n in range(1, N+1):
#         lst.append((1 + (1 / n))**n)
#         sum = sum + lst[i]
#         i = i + 1
#     return sum


# n = new_list(int(input('Введите число: ')))
# print(round(n, 3))




n = int(input('Введите число: '))

print(sum(list(map(lambda i: round( ((1 + 1/i)**i), 3), [i for i in range(1, n+1)])))) 
