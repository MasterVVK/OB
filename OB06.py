# Задание: Разработать консольную игру "Битва героев" на Python с использованием классов и
# разработать план проекта по этапам/или создать kanban доску для работы над данным проектом
#
# Общее описание:
# Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с различными характеристиками.
# Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.
#
# Требования:
# Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# Игра должна быть реализована как консольное приложение.
#
# Классы:
#
# Класс Hero:
# Атрибуты:
# Имя (name)
# Здоровье (health), начальное значение 100
# Сила удара (attack_power), начальное значение 20
# # Методы:
# attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
# is_alive(): возвращает True, если здоровье героя больше 0, иначе False
#
# Класс Game:
# Атрибуты:
# Игрок (player), экземпляр класса Hero
# Компьютер (computer), экземпляр класса Hero
# Методы:
# start(): начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет.
# Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.

import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power*random.randint(1,4)
        print(f"{self.name} атакует {other.name}, нанося {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        self.player = Hero("Игрок")
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        turn = 0

        while self.player.is_alive() and self.computer.is_alive():
            print(f"\nРаунд {turn + 1}")
            if turn % 2 == 0:
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)

            print(f"Здоровье игрока: {self.player.health}")
            print(f"Здоровье компьютера: {self.computer.health}")
            turn += 1

        if self.player.is_alive():
            print("\nИгрок победил!")
            if self.computer.health <0:
                print("\nЗапчасти Компьютера развеяны на атомы!")
        else:
            print("\nКомпьютер победил!")
            if self.player.health <0:
                print("\nПрах Игрока развеян!")

        print("Игра окончена.")


game = Game()
game.start()
