class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
            print(f"Пополнение на {amount} успешно. Новый баланс: {self.balance}")
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            print(f"Снятие {amount} успешно. Новый баланс: {self.balance}")
        else:
            print("Недостаточно средств на счете.")

    def get_balance(self):

        return self.balance


class Client:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def open_account(self, account_number, initial_deposit=0):
        new_account = Account(account_number, initial_deposit)
        self.accounts.append(new_account)
        print(f"Счет с номером {account_number} открыт для клиента {self.name}. Начальный баланс: {initial_deposit}")

    def get_accounts(self):
        return self.accounts

    def get_total_balance(self):
        total_balance = sum(account.get_balance() for account in self.accounts)
        return total_balance


client = Client("Иван Иванов")
client.open_account("123456", 1000)
client.open_account("654321", 500)

account = client.get_accounts()[0]
account.deposit(200)
account.withdraw(150)

print(" {client.name}: {client.get_total_balance()}")