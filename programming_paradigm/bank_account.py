class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        self._account_balance = float(initial_balance)

    @property
    def account_balance(self) -> float:
        return self._account_balance

    def deposit(self, amount: float) -> None:
        if amount is None:
            raise ValueError("Amount must be provided.")
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount.")
        self._account_balance += float(amount)

    def withdraw(self, amount: float) -> bool:
        if amount is None:
            raise ValueError("Amount must be provided.")
        if amount < 0:
            raise ValueError("Cannot withdraw a negative amount.")
        if amount <= self._account_balance:
            self._account_balance -= float(amount)
            return True
        return False

    def display_balance(self) -> None:
        print(f"Current Balance: ${self._account_balance:.2f}")
