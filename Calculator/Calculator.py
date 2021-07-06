from Calculator.Operations.operations import Operations


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = Operations.addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = Operations.subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = Operations.multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = Operations.division(a, b)
        return self.result

    def square(self, a):
        self.result = Operations.square(a)
        return self.result

    def squareroot(self, a):
        self.result = Operations.square_root(a)
        return self.result