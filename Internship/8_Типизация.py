# Написать функцию с аннотациями типов для аргументов и возвращаемого значения.

def introduce(name: str) -> str:
    return f"Hello, my name is {name}"


name: str = input('Introduce yourself: ')
print(introduce(name))