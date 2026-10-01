import sys
from bank_system.services import BankService


def display_menu() -> None:
    print("\n=== СИСТЕМА БАНКІВСЬКИХ РАХУНКІВ ===")
    print("1. Створити новий рахунок")
    print("2. Поповнити рахунок")
    print("3. Списати кошти з рахунку")
    print("4. Перевірити баланс рахунку")
    print("5. Пошук рахунку за номером або ім'ям")
    print("6. Показати загальну суму коштів у банку")
    print("7. Вийти з програми")


def main() -> None:
    bank_service = BankService()

    # Початкові тестові дані
    bank_service.create_account("UA1001", "Шевченко Тарас", 1500.0)
    bank_service.create_account("UA1002", "Українка Леся", 3200.5)

    while True:
        display_menu()
        choice = input("Оберіть дію (1-7): ").strip()

        if choice == "1":
            acc_num = input("Введіть номер рахунку (наприклад, UA1003): ").strip()
            owner = input("Введіть ПІБ власника: ").strip()
            try:
                initial_bal = float(input("Введіть початковий баланс (грн): "))
                acc = bank_service.create_account(acc_num, owner, initial_bal)
                print(f"Успішно створено рахунок {acc.account_number} для {acc.owner_name}!")
            except ValueError as err:
                print(f"Помилка створення: {err}")

        elif choice == "2":
            acc_num = input("Введіть номер рахунку: ").strip()
            acc = bank_service.find_account_by_number(acc_num)
            if not acc:
                print("Рахунок не знайдено.")
                continue
            try:
                amount = float(input("Введіть суму поповнення (грн): "))
                acc.deposit(amount)
                print(f"Рахунок поповнено! Поточний баланс: {acc.balance:.2f} грн.")
            except ValueError as err:
                print(f"Помилка: {err}")

        elif choice == "3":
            acc_num = input("Введіть номер рахунку: ").strip()
            acc = bank_service.find_account_by_number(acc_num)
            if not acc:
                print("Рахунок не знайдено.")
                continue
            try:
                amount = float(input("Введіть суму списання (грн): "))
                acc.withdraw(amount)
                print(f"Списання успішне! Новий баланс: {acc.balance:.2f} грн.")
            except ValueError as err:
                print(f"Помилка: {err}")

        elif choice == "4":
            acc_num = input("Введіть номер рахунку: ").strip()
            acc = bank_service.find_account_by_number(acc_num)
            if acc:
                print(f"Рахунок: {acc.account_number} | Власник: {acc.owner_name} | Баланс: {acc.balance:.2f} грн.")
            else:
                print("Рахунок не знайдено.")

        elif choice == "5":
            query = input("Введіть номер рахунку або ім'ям клієнта для пошуку: ").strip()
            by_num = bank_service.find_account_by_number(query)
            by_name = bank_service.search_accounts_by_owner(query)

            found_accounts = []
            if by_num:
                found_accounts.append(by_num)
            for acc in by_name:
                if acc not in found_accounts:
                    found_accounts.append(acc)

            if found_accounts:
                print("\nЗнайдені рахунки:")
                for acc in found_accounts:
                    print(f"- {acc.account_number} ({acc.owner_name}): {acc.balance:.2f} грн.")
            else:
                print("Рахунків за вашим запитом не знайдено.")

        elif choice == "6":
            total = bank_service.get_total_funds()
            print(f"\nЗагальна сума коштів усіх клієнтів у банку: {total:.2f} грн.")

        elif choice == "7":
            print("Завершення роботи системи. До побачення!")
            sys.exit(0)

        else:
            print("Некоректний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()