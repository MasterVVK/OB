# Создай класс Store:
#
# -Атрибуты класса:
# name: название магазина.
# address: адрес магазина.
# items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
#
# Методы класса:
# __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь дляitems`.
# -  метод для добавления товара в ассортимент.
# метод для удаления товара из ассортимента.
# метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
# метод для обновления цены товара.
#
# 2. Создай несколько объектов класса Store:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
#
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, price):
        if item_name in self.items:
            self.items[item_name] = price

store1 = Store("Магазин №1", "ул. Ленина 1")
store2 = Store("Магазин №2", "ул. Ленина 2")
store3 = Store("Магазин №3", "ул. Ленина 3")

store1.add_item("apples", 120)
store1.add_item("bananas", 150)

store2.add_item("milk", 100)
store2.add_item("bread", 50)

store3.add_item("laptop", 70000)
store3.add_item("mouse", 2500)

store1.add_item("oranges", 210)
print(f"Добавили - oranges\n{store1.items}\n")

store1.update_price("apples", 130)
print("Новая цена apples",store1.get_price("apples"))

print(f"\nУдаляем - bananas\nБыло:{store1.items}")
store1.remove_item("bananas")
print(f"Стало:{store1.items}\n")

print(f"Запрос прайса несуществующего товара:")
print(store1.get_price("milk"))
