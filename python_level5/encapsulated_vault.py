class Vault:
    def __init__(self):
        self.__pin = None
        self.__balance = 0
    def set_pin(self, pin):
        self.__pin = pin
        print("PIN set successfully.")
    def check_balance(self, pin):
        if pin == self.__pin:
            print("Balance:", self.__balance)
        else:
            print("Access Denied")
    def deposit(self, pin, amount):
        if pin == self.__pin:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Access Denied")
vault = Vault()
vault.set_pin(1234)
vault.deposit(1234, 5000)
vault.check_balance(1234)
vault.check_balance(1111)