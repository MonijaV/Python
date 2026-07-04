class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
    def get_statement(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: ₹{self.balance}")
account = BankAccount("Monii")
account.deposit(5000)
account.withdraw(2000)
account.withdraw(4000)
account.get_statement()