class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: Rs.{self.balance:.2f}"

    def deposit_balance(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs. {amount:.2f} has been deposited to your account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw_balance(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Rs.{amount:.2f} has been withdrawn from your account.")


class Bank:
    def __init__(self):
        self.bank_accounts = []

    def add_bank_account(self, bank_account):
        self.bank_accounts.append(bank_account)

    def display_bank_accounts(self):
        if not self.bank_accounts:
            print("No bank accounts available.")
            return
        for bank_account in self.bank_accounts:
            print(bank_account)

    def deposit(self, account_number, amount):
        for account in self.bank_accounts:
            if account.account_number == account_number:
                account.deposit_balance(amount)
                return
        print("Account not found.")

    def withdraw(self, account_number, amount):
        for account in self.bank_accounts:
            if account.account_number == account_number:
                account.withdraw_balance(amount)
                return
        print("Account not found.")

    def account_details(self, account_number):
        for account in self.bank_accounts:
            if account.account_number == account_number:
                print(account)
                return
        print("Account not found.")


def main():
    bank = Bank()

    while True:
        print("\nBank Menu")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Display Account Details")
        print("4. Display All Bank Accounts")
        print("5. Add Bank Account")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to deposit: "))
                bank.deposit(account_number, amount)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        elif choice == '2':
            account_number = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to withdraw: "))
                bank.withdraw(account_number, amount)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        elif choice == '3':
            account_number = input("Enter account number: ")
            bank.account_details(account_number)

        elif choice == '5':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            bank.add_bank_account(BankAccount(account_number, account_holder))
            print(f"Account no.{account_number} added.")

        elif choice == '4':
            print("\nAll Bank Accounts:")
            bank.display_bank_accounts()

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
