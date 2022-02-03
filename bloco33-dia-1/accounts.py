from customers import Customer


class Account():
    def __init__(self, customers, number, balance=0):
        self._balance = balance
        self._customers = customers
        self._number = number
        self._transactions = []
        self.deposit(balance)

    def status(self):
        print(f"Número da conta: {self._number} Saldo: {self._balance:10.2f}")

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance += -amount
            self._transactions.append(['SAQUE', amount])

    def deposit(self, amount):
        self._balance += amount
        self._transactions.append(['DEPOSITO', amount])

    def details(self):
        print(f"Extrato da conta número: {self._number}\n ")
        for t in self._transactions:
            print(f"{t[0]:10s} {t[1]:10.2f}")
        print(f"\n Saldo: {self._balance:10.2f}\n")


client1 = Customer('thiago leite', 'thiagoleite@email.com')

conta1 = Account([client1], '1234', 100)

conta1.deposit(20)
conta1.status()
conta1.withdraw(92)
conta1.status()

conta1.details()
