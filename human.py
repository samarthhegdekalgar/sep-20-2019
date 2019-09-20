class Human:
    def __init__(self, height, weight, color):
        self.height = height
        self.weight = weight
        self.color = color

    def get_detail(self):
        return self.height, self.weight, self.color


class Male(Human):
    def __init__(self, name):
        self.name = name

    def get_detail(self):
        return self.name


class Female(Human):
    def __init__(self, name):
        self.name = name

    def get_detail(self):
        return self.name