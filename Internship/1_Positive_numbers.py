## Создайте тип данных, который может хранить только числа больше нуля

class PositiveNumber(int):
    def __new__(cls, value):
        if isinstance(value, int) and value > 0:
            instance = super().__new__(cls, value)
        else:
            raise ValueError("Input must be a positive integer")
        return instance


a = PositiveNumber(10)
b = PositiveNumber(10)
c = a + b
print(c)

