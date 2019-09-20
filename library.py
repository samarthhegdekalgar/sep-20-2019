class Library:
    def __init__(self, location, status):
        self.location = location
        self.status = status
        self.book = []
        self.staff = []
        self.customer = []

    def add_book(self, book_obj):
        self.book.append(book_obj)

    def add_staff(self, staff_obj):
        self.staff.append(staff_obj)

    def add_customer(self, customer_obj):
        self.customer.append(customer_obj)


class Book:
    def __init__(self, name, price, no_of_copy):
        self.name = name
        self.price = price
        self.no_of_copy = no_of_copy


class Customers:
    def __init__(self, id, name, deposit, borrowed_books):
        self.id = id
        self.name = name
        self.deposit = deposit
        self.borrowed_books = borrowed_books


class Staff:
    def __init__(self, id, name, salary, work_hours):
        self.id = id
        self.name = name
        self.salary = salary
        self.work_hours = work_hours


staff_obj = Staff(1,'samarth', 99999, 8)
customer_obj = Customers(1,'Varun', 9999, 10)
head_first_python = Book('Head First Python', 945, 8)
library_obj = Library('Banglore', 'Closed')
library_obj.add_customer(customer_obj)
library_obj.add_book(head_first_python)
library_obj.add_staff(staff_obj)
print(f"Library location : {library_obj.location}")
print(f"Library Status: {library_obj.status}")
print(f"Staff name: {staff_obj.name}")
print(f"Staff salary: {staff_obj.salary}")
print(f"Customer name : {customer_obj.name}")
print(f"Number of book taken: {customer_obj.borrowed_books}")