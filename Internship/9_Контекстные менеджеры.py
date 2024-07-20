# Написать программу, которая открывает файл для чтения,
# читает его содержимое и закрывает файл автоматически с
# использованием with.


with open('example.txt') as file:
    content = file.read()
    print(content)

