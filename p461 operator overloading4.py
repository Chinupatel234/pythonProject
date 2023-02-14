class Multiply:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        result = self.a * other.a
        result1 = self.b * other.b
        return result, result1


obj = Multiply(11, 22)
obj1 = Multiply(2, 3)
print("The sum is: ", obj * obj1)
