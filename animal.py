class Animal:
    def __init__(self, no_of_leg, no_of_wing, isswim, isfly, isrun):
        self.no_of_leg =  no_of_leg
        self.no_of_wing = no_of_wing
        self.isswim = isswim
        self.isfly = isfly
        self.isrun = isrun

    def get_detail(self):
        return self.no_of_leg, self.no_of_wing, self.isswim, self.isrun, self.isfly


class Cat(Animal):
    def __init__(self, name, type_of_sound, color):
        self.name = name
        self.type_of_sound = type_of_sound
        self.color = color

    def get_datail(self):
        return self.name, self.type_of_sound, self.color


class Dog(Animal):
    def __init__(self, name, type_of_sound, color):
        self.name = name
        self.type_of_sound = type_of_sound
        self.color = color

    def get_datail(self):
        return self.name, self.type_of_sound, self.color


class Fish(Animal):
    def __init__(self, name, type_of_sound, color):
        self.name = name
        self.type_of_sound = type_of_sound
        self.color = color

    def get_datail(self):
        return self.name, self.type_of_sound, self.color


fish = Fish('Samarth', 'trrrrr', 'red')
print(fish.super().get_datail())