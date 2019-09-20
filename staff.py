class Staff:
    def __init__(self, id, type):
        self.id = id
        self.type = type

    def get_detail(self):
        return self.id, self.type


class Teacher(Staff):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_detail(self):
        return self.name, self.salary


class Principal(Staff):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_detail(self):
        return self.name, self.salary
