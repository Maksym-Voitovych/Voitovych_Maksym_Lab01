from dataclasses import dataclass


@dataclass
class BankAccount:
    """Модель банківського рахунку.
    
    Забороняє встановлення або зміну балансу до від'ємного значення.
    """
    account_number: str
    owner_name: str
    balance: float = 0.0

    def deposit(self, amount: float) -> None:
        """Поповнення рахунку."""
        if amount <= 0:
            raise ValueError("Сума поповнення повинна бути більшою за нуль.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Списання коштів з рахунку."""
        if amount <= 0:
            raise ValueError("Сума списання повинна бути більшою за нуль.")
        if amount > self.balance:
            raise ValueError(
                f"Недостатньо коштів! Поточний баланс: {self.balance:.2f} грн. "
                "Від'ємний баланс заборонено."
            )
        self.balance -= amount