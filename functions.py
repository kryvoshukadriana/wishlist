import json
import os

FOLDER = "data"
FILEPATH = "data/wishlist.json"

def load_items():
    """Завантажує список бажань із JSON-файлу або повертає порожній список."""
    if not os.path.exists(FILEPATH) or os.path.getsize(FILEPATH) == 0:
        return []
    try:
        with open(FILEPATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []

def save_items(items):
    """Зберігає список бажань у JSON-файл."""
    os.makedirs(FOLDER, exist_ok=True)
    with open(FILEPATH, "w", encoding="utf-8") as file:
        json.dump(items, file, ensure_ascii=False, indent=4)

def check_number(number_text, items):
    """Перевіряє коректність номера бажання в списку."""
    if not number_text.isdigit():
        print("Помилка: номер має бути цілим числом.")
        return None
    number = int(number_text)
    if not 1 <= number <= len(items):
        print(f"Помилка: бажання під номером {number} не існує.")
        return None
    return number

def add_item(argument):
    """Додає бажання (можна вказати лише назву або 'назва | ціна')."""
    argument = argument.strip()
    if not argument:
        print("Помилка: назва бажання не може бути порожньою.")
        return

    # Якщо передали ціну через розділювач '|'
    if "|" in argument:
        parts = argument.split("|", maxsplit=1)
        title = parts[0].strip()
        price_str = parts[1].strip()
        try:
            price = float(price_str)
        except ValueError:
            print("Помилка: ціна повинна бути числом.")
            return
    else:
        title = argument
        price = 0.0

    if not title:
        print("Помилка: назва бажання не може бути порожньою.")
        return

    items = load_items()
    items.append({"title": title, "price": price, "bought": False})
    save_items(items)
    print(f"Бажання «{title}» ({price} грн) додано у список.")

def show_items():
    """Виводить увесь список бажань із цінами та статусом купівлі."""
    items = load_items()
    if not items:
        print("Ваш список бажань порожній.")
        return
    print("\n=== Ваш Wishlist ===")
    for index, item in enumerate(items, start=1):
        status = "Куплено" if item.get("bought") else "Хочу"
        price = item.get("price", 0.0)
        print(f"{index}. [{status}] {item['title']} — {price:.2f} грн")

def mark_bought(number_text):
    """Позначає річ як куплену."""
    items = load_items()
    number = check_number(number_text, items)
    if number is None:
        return
    items[number - 1]["bought"] = True
    save_items(items)
    print(f"Вітаємо! Бажання #{number} «{items[number - 1]['title']}» куплено!")

def delete_item(number_text):
    """Видаляє пункт зі списку бажань."""
    items = load_items()
    number = check_number(number_text, items)
    if number is None:
        return
    removed = items.pop(number - 1)
    save_items(items)
    print(f"Бажання «{removed['title']}» видалено зі списку.")

def show_total():
    """Рахує, скільки грошей потрібно на некуплені бажання."""
    items = load_items()
    unbought_total = sum(item.get("price", 0.0) for item in items if not item.get("bought"))
    bought_total = sum(item.get("price", 0.0) for item in items if item.get("bought"))
    print("\n--- Фінансовий підсумок ---")
    print(f"Ще потрібно зібрати: {unbought_total:.2f} грн")
    print(f"Вже витрачено на здійснені мрії: {bought_total:.2f} грн")