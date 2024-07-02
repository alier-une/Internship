# 1 Написать программу, которая использует while цикл для подсчета суммы чисел от 1 до 100.
def digit_sum(start, end):
    counter = 0
    while start <= end:
        counter += start
        start += 1
    return counter

start, end = 1, 100
#print('Сумма чисел:', digit_sum(start, end))

# 2 Написать функцию, которая принимает список чисел и возвращает два списка отсортированных по четному и нечетному числу
def sort_lists(my_list):
    even = sorted([el for el in my_list if el % 2 == 0])
    odd = sorted([el for el in my_list if el % 2 == 1])
    return f'Четный список: {even}, \nНечетный список: {odd}'

my_list = [3, 5, 7, 6, 4, 2, 45, 23, 76, 2, 9, 66]
#print(sort_lists(my_list))

# 3 Написать программу, которая генерирует все простые числа в диапазоне от 1 до 100 с использованием цикла for.
def prime_num(start, end):
    prime_list = []
    for i in range(start, end + 1):
        dividers = [d for d in range(start, i + 1) if i % d == 0]
        if len(dividers) == 2:
            prime_list.append(i)
        else:
            continue
    return prime_list

start, end = 1, 100
#print('Список простых чисел: ', prime_num(start, end))

# 4 Написать программу, которая использует цикл while для подсчета факториала числа, введенного пользователем.
def get_factorial(user_input):
    factorial = 1
    while user_input > 0:
        factorial *= user_input
        user_input = user_input - 1
    return factorial

#user_input = int(input("Введите ваше число: "))
#print(get_factorial(user_input))

# 5 Написать генератор, который возвращает бесконечную последовательность чисел Фибоначчи.
def fibonacci_number():
    fib_1, fib_2 = 0, 1
    while True:
        yield fib_1
        fib_1, fib_2 = fib_2, fib_1 + fib_2

for fib in fibonacci_number():
    print(fib)