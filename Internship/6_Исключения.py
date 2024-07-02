# Написать программу, которая запрашивает у пользователя ввод числа и обрабатывает возможное исключение при неверном
# вводе.
try:
    n = int(input('Введите число: '))
except ValueError:
    print('Ошибка: введено не числовое значение')
else:
    print('Операция успешно выполнена')


# Написать функцию, которая делит два числа и обрабатывает исключение деления на ноль.
def division(a, b):
    try:
        c = a / b
        print(f'Результат: {c}')
    except ZeroDivisionError:
        print('Ошибка: деление на ноль')


division(45, 0)

# Написать программу, которая считывает содержимое файла и обрабатывает возможные исключения,
# такие как FileNotFoundError и PermissionError.
# (если есть трудности, прочтите тему контекстных менеджеров и можете возвращаться)

file = open('example.txt')
try:
    print('Success')
except FileNotFoundError:
    print('Error: file not found')
finally:
    file.close()