import functions

def print_help():
    print("\nДоступні команди:")
    print("  add <назва> | <ціна>   - додати бажання (наприклад: add Кросівки | 3200)")
    print("  show                   - показати список бажань")
    print("  bought <номер>         - позначити річ купленою")
    print("  delete <номер>         - видалити бажання")
    print("  total                  - порахувати загальну вартість")
    print("  exit                   - вийти з програми")

def main():
    print("=== My Wishlist CLI ===")
    print_help()

    while True:
        user_input = input("\n> ").strip()
        if not user_input:
            continue

        parts = user_input.split(maxsplit=1)
        command = parts[0].lower()
        argument = parts[1].strip() if len(parts) > 1 else ""

        if command == "add":
            functions.add_item(argument)
        elif command == "show":
            functions.show_items()
        elif command == "bought":
            functions.mark_bought(argument)
        elif command == "delete":
            functions.delete_item(argument)
        elif command == "total":
            functions.show_total()
        elif command == "exit":
            print("Мрії мають здійснюватися! До побачення!")
            break
        else:
            print("Невідома команда.")
            print_help()

if __name__ == "__main__":
    main()