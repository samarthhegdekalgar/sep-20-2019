class Bank:
    def __init__(self):
        self.name = 'HDFC'
        self.customers = []
        self.total_balance = 0

    def add_customer(self, customer):
        self.customers.append(customer)

    def show_all_customers(self):
        for customer in self.customers:
            print(customer.name)


class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.account = Account()


class Account:
    def __init__(self):
        self.balance = 0

    def withdraw(self, money):
        self.balance -= money

    def deposit(self, money):
        self.balance += money


sam = Customer('samarth', 'bbb')
varun = Customer('varun', 'Pune')

print(sam.account.balance)
sam.account.withdraw(1000)
print(sam.account.balance)
hdfc_bank = Bank()
hdfc_bank.add_customer(sam)
hdfc_bank.add_customer(varun)
Bank.show_all_customers(hdfc_bank)
hdfc_bank.show_all_customers()