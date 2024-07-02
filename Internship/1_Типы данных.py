## 1 Создать список из нескольких чисел и строк, затем разделить его на два списка: один для чисел, другой для строк.
def divide_lists(my_list):
    digits = [d for d in my_list if type(d) == int]
    words = [w for w in my_list if type(w) == str]
    return digits, words


my_list = [1, 2, 'hello', 56, 'python', 33, 'red']
print(divide_lists(my_list))


## 2 Написать программу, которая подсчитывает количество уникальных слов в тексте, введенном пользователем.
## Вывести статистику по количеству уникальных слов и общее количество слов.


def unic_words(user_input):
    text = str(user_input).lower().split()
    # Пример текста: Привет, как дела? привет. Ты сам КАК???? да норм, пРивЕт.
    final_text = []
    signs = '.,?!:;-()'

    for word in text:
        if word.isdigit() or word.isalpha() == True:
            final_text.append(word)
        else:
            for sign in signs:
                if sign in word:
                    word = word.replace(sign, '')
                    final_text.append(word)
                    break

    return f'Количество уникальных слов: {len(set(final_text))} \nОбщее количество слов: {len(final_text)}'


# user_input = input('Введите ваш текст: ')
# print(unic_words(user_input))

## для интересующихся (необязательно): Создайте тип данных, который может хранить только числа больше нуля
def positive(number):
    if number < 0:
        raise ValueError('Число должно быть больше нуля')
    else:
        return number


n = positive(9)
print(n)
