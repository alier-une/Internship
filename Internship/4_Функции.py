# 1 Написать функцию, которая принимает список чисел и возвращает их среднее значение.
def avg(my_list):
    return sum(my_list) / len(my_list)
my_list = [1, 2, 3, 4, 5]
print(avg(my_list))

# 2 Написать функцию, которая принимает список строк и возвращает словарь, где ключи — это длины строк,
# а значения — списки строк соответствующей длины.
def make_dict(my_list):
    dictionary = dict()
    lens = list(set([len(x) for x in my_list]))
    for i in range(len(lens)):
        dictionary[lens[i]] = [s for s in my_list if len(s) == lens[i]]
    return dictionary

my_list = ['cat', 'table', 'dog', 'pet', 'flower', 'finger']
print(make_dict(my_list))