class Parent:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"Значение: {self.value}")


class Child(Parent):
    def __init__(self, value, child_value):
        super().__init__(value)  # Вызов конструктора суперкласса
        self.child_value = child_value

    def show(self):
        super().show()  # Вызов метода суперкласса
        print(f"Дочернее значение: {self.child_value}")


# Использование
child = Child(10, 20)
child.show()
