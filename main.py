# 1. Single Responsibility Principle (Принцип единственной ответственности)
# Принцип гласит, что класс должен иметь только одну причину для изменения.

# Плохо: класс выполняет две задачи - управление пользователями и их аутентификацией
class User:
    def __init__(self, name: str):
        self.name = name

    def add_user(self, user):
        pass  # Добавление пользователя

    def authenticate_user(self, user):
        pass  # Аутентификация пользователя

# Хорошо: разделение ответственности на два класса
class UserManager:
    def add_user(self, user):
        pass  # Добавление пользователя

class Authenticator:
    def authenticate_user(self, user):
        pass  # Аутентификация пользователя

# 2. Open/Closed Principle (Принцип открытости/закрытости)
# Принцип гласит, что классы должны быть открыты для расширения, но закрыты для модификации.

# Плохо: добавление нового типа уведомления требует изменения класса Notification
class Notification:
    def send(self, message, type):
        if type == "email":
            # Отправка email
            pass
        elif type == "sms":
            # Отправка SMS
            pass

# Хорошо: использование абстракции для расширения возможностей без изменения существующего кода
class NotificationSender:
    def send(self, message):
        pass

class EmailNotificationSender(NotificationSender):
    def send(self, message):
        # Отправка email
        pass

class SMSNotificationSender(NotificationSender):
    def send(self, message):
        # Отправка SMS
        pass

# 3. Liskov Substitution Principle (Принцип подстановки Лисков)
# Объекты в программе должны быть заменяемы на экземпляры их подтипов без изменения корректности программы.

# Хорошо: подкласс может служить заменой для своего суперкласса
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        pass

def make_bird_fly(bird: Bird):
    bird.fly()

sparrow = Sparrow()
make_bird_fly(sparrow)  # Корректно, Sparrow является подтипом Bird

# 4. Interface Segregation Principle (Принцип разделения интерфейса)
# Клиенты не должны быть вынуждены зависеть от интерфейсов, которые они не используют.
# Плохо: один большой интерфейс
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

# Хорошо: разделение на более мелкие интерфейсы
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Worker(Workable, Eatable):
    def work(self):
        pass

    def eat(self):
        pass

# 5. Dependency Inversion Principle (Принцип инверсии зависимостей)
# Модули высокого уровня не должны зависеть от модулей низкого уровня. Оба типа модулей должны зависеть от абстракций.

# Плохо: класс высокого уровня зависит от класса низкого уровня
class LightBulb:
    def turn_on(self):
        pass

class Switch:
    def __init__(self, bulb: LightBulb):
        self.bulb = bulb

# Хорошо: оба класса зависят от абстракций
class Switchable:
    def turn_on(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        pass

class Switch:
    def __init__(self, device: Switchable):
        self.device = device
