class Fraction:

    def __init__(self, counter, denominator):
        self.counter = counter
        self.denominator = denominator

    def __str__(self):
        return f'{self.counter}/{self.denominator}'

    def __add__(self):
        return self.counter + self.denominator

    def __sub__(self):
        return self.counter - self.denominator

    def inverse(self):
        return self.denominator / self.counter
