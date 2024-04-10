# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`,
# `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()`
# для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и возможность её загрузки,
# чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

import json
import pickle


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Что-то озвучить"

    def eat(self):
        return f"{self.name} ест."

class Bird(Animal):
    def make_sound(self):
        return "Птичка щебечет"

class Mammal(Animal):
    def make_sound(self):
        return "Млекопитающие ревёт"

class Reptile(Animal):
    def make_sound(self):
        return "Пресмыкающееся шипит"
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, person):
        self.staff.append(person)

    def show_animals(self):
        for animal in self.animals:
            print(f"Животное: {animal.name}, Возраст: {animal.age}")

    def show_staff(self):
        for person in self.staff:
            print(f"Работник: {person.name}, Роль: {person.role}")


class ZooKeeper:
    def __init__(self, name):
        self.name = name
        self.role = "ZooKeeper"

    def feed_animal(self, animal):
        print(f"{self.name} кормит живое существо: {animal.name}.")

class Veterinarian:
    def __init__(self, name):
        self.name = name
        self.role = "Veterinarian"

    def heal_animal(self, animal):
        print(f"{self.name} лечит живое существо: {animal.name}.")


animals = [Bird("Соловей", 1), Mammal("Лев", 5), Reptile("Змея", 2)]
animal_sound(animals)


zoo = Zoo()

with open('zoo.pkl', 'rb') as inp:
    zoo = pickle.load(inp)

#zoo.add_animal(Bird("Попугай", 3))
#zoo.add_animal(Mammal("Тигр", 4))

#zoo.add_staff(ZooKeeper("Алексей"))
#zoo.add_staff(Veterinarian("Иван"))

zoo.show_animals()
zoo.show_staff()

zoo.staff[0].feed_animal(zoo.animals[0])
zoo.staff[1].heal_animal(zoo.animals[1])

with open('zoo.pkl', 'wb') as outp:
    pickle.dump(zoo, outp, pickle.HIGHEST_PROTOCOL)

with open('zoo.pkl', 'rb') as inp:
    zoo_loaded = pickle.load(inp)
print(f"\nПроверка загрузки в zoo_loaded")
zoo_loaded.show_animals()
zoo_loaded.show_staff()