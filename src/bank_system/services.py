from typing import List, Optional
from bank_system.models import BankAccount


class BankService:
    """Сервіс для управління групою банківських рахунків."""

    def __init__(self) -> None:
        self.accounts: List[BankAccount] = []

    def create_account(
        self, account_number: str, owner_name: str, initial_balance: float = 0.0
    ) -> BankAccount:
        """Створення нового рахунку."""
        if self.find_account_by_number(account_number) is not None:
            raise ValueError(f"Рахунок з номером '{account_number}' вже існує.")
        if initial_balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним.")

        account = BankAccount(
            account_number=account_number,
            owner_name=owner_name,
            balance=initial_balance
        )
        self.accounts.append(account)
        return account

    def find_account_by_number(self, account_number: str) -> Optional[BankAccount]:
        """Пошук рахунку за точним номером."""
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def search_accounts_by_owner(self, owner_name: str) -> List[BankAccount]:
        """Пошук рахунків за ім'ям власника (підстрока)."""
        query = owner_name.strip().lower()
        return [
            acc for acc in self.accounts 
            if query in acc.owner_name.lower()
        ]

    def get_total_funds(self) -> float:
        """Обчислення загальної суми коштів на всіх рахунках."""
        return sum(account.balance for account in self.accounts)