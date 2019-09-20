class Bank:
    def __init__(self, name='SBI', address='Banglore', ifsc='004SBI987', total_balance=999999):
        self.name = name
        self.address = address
        self.ifsc = ifsc
        self.total_balance = total_balance

    def get_bank_detail(self):
        return f'Bank name: {self.name}\nAddress: {self.address}\n IFSC: {self.ifsc}'

    def get_available_money(self):
        return self.total_balance


class Customer(Bank):
    def __init__(self, name, account_number, account_balance=0):
        self.name = name
        self.account_number = account_number
        self.account_balance = account_balance

    def deposit(self, deposit):
        self.account_balance = self.account_balance + deposit
        Bank.total_balance += deposit
        return True

    def withdraw(self, required):
        if required < self.account_balance:
            self.account_balance = self.account_balance - required
            Bank.total_balance -= required
            return True
        else:
            return False

    def display_balance(self):
        return self.account_balance

    def display_detail(self):
        return f'Account holder name:{self.name}\n Account Number: {self.account_number}\n Balance: {self.account_balance}'


if __name__ == '__main__':
    program_status = True
    user_name = str(input("Enter your name:\t"))
    user_account_number = 987654321
    customer_obj = Customer(user_name, user_account_number)
    print(f"{user_name} your account details:")
    print(customer_obj.display_detail())
    while program_status:
        user_choice = int(input("1.Deposit\t 2.Withdraw\t 3.Balance check\t 4.Bank detail\n 5.Bank Total money\t 6.Exit"))
        if user_choice == 1:
            deposite_by_user = int(input("Enter deposit amount:\t"))
            customer_obj.deposit(deposite_by_user)
        elif user_choice == 2:
            withdraw_amount = int(input("How much money you want?:\t"))
            status = customer_obj.withdraw(withdraw_amount)
            if not status:
                print("Your account balance is low!")
        elif user_choice == 3:
            print(f" Balance: {customer_obj.display_balance()}")

        elif user_choice == 4:
            print(customer_obj.get_bank_detail())

        elif user_choice == 5:
            print(f'Bank has: {customer_obj.get_available_money()}')

        else:
            print('Good Bye!')
            program_status = False
