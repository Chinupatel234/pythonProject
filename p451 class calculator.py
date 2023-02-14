class calc():
    def __init__(self):
        print("Welcome to the Calculator...")


class mul(calc):
    def __init__(self):
        super().__init__()
        print("Multiplication")
        self.a = int(input("Enter the number1: "))
        self.b = int(input("Enter the number2: "))

    def answer(self):
        print("Multiplication: ", self.a * self.b)


class add(mul):
    def __init__(self):
        super().__init__()
        print("Addition")
        self.c = int(input("Enter the number1: "))
        self.d = int(input("Enter the number2: "))

    def answer1(self):
        print("Addition: ", self.c + self.d)


class div(add):
    def __init__(self):
        super().__init__()
        print("Division")
        self.e = int(input("Enter the number1: "))
        self.f = int(input("Enter the number2: "))

    def answer2(self):
        print("Division: ", self.e / self.f)


class sub(div):
    def __init__(self):
        super().__init__()
        print("Subtraction")
        self.g = int(input("Enter the number1: "))
        self.h = int(input("Enter the number2: "))

    def answer3(self):
        print("Subtraction: ", self.g - self.h)


calc1 = sub()
print("*"*20)
calc1.answer()
calc1.answer1()
calc1.answer2()
calc1.answer3()
print("*"*20)
