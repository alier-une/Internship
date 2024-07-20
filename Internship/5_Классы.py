# 1 Создать класс Car с атрибутами made_by,  model и методом display_info, который выводит информацию о машине.
class Car:

    def __init__(self, made_by, model):
        self.made_by = made_by
        self.model = model

    def display_info(self):
        print(f'Страна производства: {self.made_by} \nМодель машины: {self.model}')

car1 = Car('USA', 'Chevrolet Impala')
car1.display_info()


# 2 Создать класс BankAccount с атрибутами balance и методами deposit, withdraw, и get_balance.
# Реализовать контроль за достаточностью средств при снятии.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('Недостаточно средств')

    def get_balance(self):
        print(self.balance)


account = BankAccount(3330)
account.deposit(1907)
account.withdraw(666)
account.get_balance()
# 3 Дополнительное задание: На метаните (в ссылках на полезные материалы) куча прикольных практических задач, по желанию можно их сделать :)
