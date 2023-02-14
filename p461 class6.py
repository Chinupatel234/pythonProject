class Vehicle:
    def __init__(self, tyres, color):
        self.tyres = tyres
        self.color = color

    def display(self):
        print("Vehicle Class created!!!")


class Car(Vehicle):
    def __init__(self):
        self.accelerator = True
        super().__init__(5, "Pink")

    def dis(self):
        print(f"Car has {self.tyres} tyres and {self.color} color and has a {self.accelerator} accelerator")


a = Car()
a.display()
print(a.tyres)
print(a.accelerator)
a.dis()
