# Создайте классы Car, Driver
# Car свойства: mileage (пробег), is_turned_on, driver
# Driver наследуется от класса Person, опишите на своё усмотрение
# Далее, создайте контекстный менеджер, который будет
# принимать в себя аргументы car, driver, и при инициализации
# контекстного менеджера, будет включать двигатель машины,
# и каждую секунду пока двигатель активен, добавлять +1 к mileage,
# и когда мы выходим из контекста, двигатель глушился и реализуйте
# валидацию ситуации, когда пользователь пытается завести уже заведенную машину.

# Дополнительно: добавьте валидацию, что машиной может управлять только тот человек,
# чья это машина, и возвращать ошибку, если машиной начал управлять не собственник машины.
# Затем, поменяйте свойство driver, на drivers, и реализуйте логику
# чтобы собственников могло быть несколько.

# Супер-дополнительно: реализуйте метод, с помощью которого можно будет узнать каким т/c
# в данный момент управляет водитель, и какими машинами владеет

from string import ascii_letters
import time


class Person:
    S_RUS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя-"
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, age):
        self.fio = fio
        self.age: int = age

    @classmethod
    def verify_fio(cls, fio):
        if not isinstance(fio, str):
            raise TypeError("Name must be string")

        fio = fio.split()
        if len(fio) != 3:
            raise TypeError("Invalid name format. You should write your last name, "
                            "first name, and patronymic. If you don't have patronymic "
                            "write - ")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in fio:
            if len(s) < 1:
                raise TypeError("Name must contain at least one character")
            if len(s.strip(letters)) != 0:
                raise TypeError("You can use only alphabetic characters and dash")

    @classmethod
    def verify_age(cls, age):
        if not isinstance(age, int):
            raise TypeError("Age should be an integer")
        if age < 18:
            raise TypeError("You not old enough to drive a car")

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age


class Driver(Person):
    def __init__(self, fio, age):
        super().__init__(fio, age)
        super().verify_fio(fio)
        super().verify_age(age)


class Car:
    def __init__(self, car_name, driver: Driver):
        self.name = car_name
        self.mileage = 0
        self.is_turned_on: bool = False
        self.driver = driver


class StartEngine:
    def __init__(self, car: Car, driver: Driver):
        self.car = car
        self.driver = driver

    @classmethod
    def verify_engine(cls, is_turned_on):
        if is_turned_on:
            raise ValueError("Engine is already running")

    def __enter__(self):
        self.verify_engine(self.car.is_turned_on)
        self.car.is_turned_on = True
        while self.car.is_turned_on:
            print(self.car.mileage)
            time.sleep(1)
            self.car.mileage += 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.car.is_turned_on = False
        return self.car.mileage


d = Driver("John Doe -", 23)
c = Car("Toyota", d)

with StartEngine(c, d) as se:
    print(c.mileage)
