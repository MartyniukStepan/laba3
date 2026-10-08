class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

products = [Product("Ноутбук", 49999, 10), Product("Мишка", 1199, 50), Product("Клавіатура", 2499, 25), Product("Навушники", 1499, 12), Product("Мікрофон", 1799, 17), Product("Телефон", 19799, 1)]

cart = []

def show_products():
    print("\n--- КАТАЛОГ ---")
    for i in range(len(products)):
        print(i + 1, products[i].name, "-", f"{products[i].price:.2f} грн", "Залишок:", products[i].count)

def add_to_cart():
    show_products()
    number = int(input("Введіть номер товару: "))

    if number < 1 or number > len(products):
        print("Такого товару немає!")
        return

    product = products[number - 1]

    if product.count == 0:
        print("Товару немає в наявності!")
        return

    cart.append(product)
    product.count -= 1

    print("Товар додано в кошик!")


def show_cart():
    print("\n--- КОШИК ---")
    if len(cart) == 0:
        print("Кошик порожній!")
        return

    total = 0

    for i in range(len(cart)):
        print(
            i + 1,
            cart[i].name,
            "-",
            f"{cart[i].price:.2f} грн"
        )

        total += cart[i].price

    print("Всього:", f"{total:.2f} грн")


def remove_from_cart():
    show_cart()

    if len(cart) == 0:
        return

    number = int(input("Введіть номер товару для видалення: "))

    if number < 1 or number > len(cart):
        print("Неправильний номер!")
        return

    product = cart.pop(number - 1)

    product.count += 1

    print("Товар видалено з кошика!")


def buy():
    show_cart()

    if len(cart) == 0:
        return

    total = 0

    for product in cart:
        total += product.price

    print("До оплати:", f"{total:.2f} грн")

    answer = input("Купити товари? (yes/no): ")

    if answer == "yes":
        cart.clear()
        print("Покупку успішно здійснено!")
    elif answer == "no":
        print("Покупку скасовано.")
    else:
        print("Помилка")


def admin():
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    if login == "admin" and password == "1234":
        print("\n--- ЗАЛИШКИ ТОВАРІВ ---")

        for product in products:
            print(
                product.name,
                "-",
                product.count,
                "шт."
            )

    else:
        print("Неправильний логін або пароль!")


def main():
    while True:
        print("\n--- МАГАЗИН ---")
        print("1 - Каталог")
        print("2 - Додати в кошик")
        print("3 - Переглянути кошик")
        print("4 - Видалити з кошика")
        print("5 - Купити")
        print("6 - Адміністратор")
        print("0 - Вихід")
        print("---------------")
        print(" ")

        choice = input("Виберіть дію: ")

        if choice == "1":
            show_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            show_cart()
        elif choice == "4":
            remove_from_cart()
        elif choice == "5":
            buy()
        elif choice == "6":
            admin()
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Неправильний вибір!")
main()
