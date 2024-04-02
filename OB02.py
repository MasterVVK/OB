# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
#
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа,
# специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user,
# которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).


class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._user_list = []

    def add_user(self, user):
        if not self._is_user_exist(user):
            self._user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print(f"Пользователь {user.get_name()} такой уже есть.")

    def remove_user(self, user):
        if self._is_user_exist(user):
            self._user_list.remove(user)
            print(f"Пользователь {user.get_name()} удален.")
        else:
            print(f"Пользователь {user.get_name()} для удаления, не найден.")

    def _is_user_exist(self, user):
        return user in self._user_list


user1 = User("1", "Юзверь1")
user2 = User("2", "Юзверь2")
admin = Admin("admin1", "Просто Админ")

admin.add_user(user1)
admin.add_user(user2)

admin.add_user(user1)

admin.remove_user(user1)

admin.remove_user(user1)
