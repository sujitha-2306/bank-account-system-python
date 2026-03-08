from abc import ABC, abstractmethod
from datetime import datetime

# ==============================
# Abstract Base Class
# ==============================
class BankAccount(ABC):

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self._transactions = []   # transaction history

    # Abstraction
    @abstractmethod
    def account_type(self):
        pass

    # Encapsulation (controlled access)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._add_transaction(f"Deposited ₹{amount}")
            print("✅ Deposited:", amount)
        else:
            print("❌ Invalid deposit amount")

    def withdraw(self, amount):
        if self._can_withdraw(amount):
            self.__balance -= amount
            self._add_transaction(f"Withdrawn ₹{amount}")
            print("✅ Withdrawn:", amount)
        else:
            print("❌ Withdrawal denied")

    def get_balance(self):
        return self.__balance

    def show_transactions(self):
        print("\n📜 Transaction History:")
        for t in self._transactions:
            print(t)

    def save_transactions_to_file(self):
        filename = f"{self.name}_transactions.txt"
        with open(filename, "w") as f:
            for t in self._transactions:
                f.write(t + "\n")
        print("💾 Transactions saved to file")

    def _add_transaction(self, message):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._transactions.append(f"{time} - {message}")

    @abstractmethod
    def _can_withdraw(self, amount):
        pass

# ==============================
# Savings Account
# ==============================
class SavingsAccount(BankAccount):

    MIN_BALANCE = 500

    def account_type(self):
        return "Savings Account"

    def _can_withdraw(self, amount):
        if self.get_balance() - amount >= SavingsAccount.MIN_BALANCE:
            return True
        else:
            print("⚠ Minimum balance of ₹500 must be maintained")
            return False

# ==============================
# Current Account
# ==============================
class CurrentAccount(BankAccount):

    OVERDRAFT_LIMIT = 2000

    def account_type(self):
        return "Current Account"

    def _can_withdraw(self, amount):
        if self.get_balance() + CurrentAccount.OVERDRAFT_LIMIT >= amount:
            return True
        else:
            print("⚠ Overdraft limit exceeded")
            return False

# ==============================
# Menu Driven System
# ==============================
def main():

    print("🏦 Welcome to Simple Bank System")

    name = input("Enter Account Holder Name: ")
    acc_type = input("Choose Account Type (1-Savings / 2-Current): ")
    balance = float(input("Enter Initial Balance: "))

    if acc_type == "1":
        account = SavingsAccount(name, balance)
    else:
        account = CurrentAccount(name, balance)

    print(f"\n🎉 {account.account_type()} Created Successfully!")

    while True:
        print("\n------ MENU ------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Show Transactions")
        print("5. Save Transactions to File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == "3":
            print("💰 Current Balance:", account.get_balance())

        elif choice == "4":
            account.show_transactions()

        elif choice == "5":
            account.save_transactions_to_file()

        elif choice == "6":
            print("👋 Thank you for banking with us!")
            break

        else:
            print("❌ Invalid choice")


# Run Program
if __name__ == "__main__":
    main()
