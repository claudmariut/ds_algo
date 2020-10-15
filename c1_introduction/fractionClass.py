def gcd(m, n):
    """Returns gdc using Euclid's Algorithm"""
    while m % n != 0:
        oldm = m
        oldn = n

        n = oldm % oldn
        m = oldn
    return n


class Fraction:
    """Represent data objects that look like fractions."""
    def __init__(self, top, bottom):  # state part
        """Initialize attributes"""
        if not (isinstance(top, int) and isinstance(bottom, int)):
            raise ValueError("Invalid Integers")
        if bottom < 0:
            bottom *= -1
            top *= -1
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def getNum(self):
        """Return numerator."""
        return self.num

    def getDen(self):
        """Return denominator."""
        return self.den

    def __str__(self):
        """Return when a Fraction object is asked."""
        return f"This is an object of the class"

    def __add__(self, other_fraction):  # Second parameter is another instance
        """Returns the sum of two fractions"""
        num = (self.num * other_fraction.den) + (other_fraction.num * self.den)
        den = self.den * other_fraction.den
        common = gcd(num, den)
        return f"{num//common}/{den//common}"

    def __eq__(self, other_fraction):
        """Returns True if both fractions are equal."""
        first_product = self.num * other_fraction.den
        second_product = self.den * other_fraction.num

        return first_product == second_product

    def __sub__(self, other):
        """Returns subtraction between two fractions."""
        num = (self.num * other.den) - (other.num * self.den)
        den = self.den * other.den
        common = gcd(num, den)
        return f"{num // common}/{den // common}"

    def __mul__(self, other):
        """Returns multiplication between two fractions."""
        num = self.num * other.num
        den = self.den * other.den
        return f"{num}/{den}"

    def __truediv__(self, other):
        """Returns division between two fractions."""
        num = self.num * other.den
        den = self.den * other.num
        common = gcd(num, den)
        return f"{num // common}/{den // common}"

    def __gt__(self, other):
        """Checks if a fraction is greater than the other."""
        f1 = self.num / self.den
        f2 = other.num / other.den

        return f1 > f2

    def __ge__(self, other):
        """Checks if a fraction is greater or equal than the other."""
        f1 = self.num / self.den
        f2 = other.num / other.den

        return f1 >= f2

    def __lt__(self, other):
        """Checks if a fraction is less than the other."""
        f1 = self.num / self.den
        f2 = other.num / other.den

        return f1 < f2

    def __le__(self, other):
        """Checks if a fraction is less than the other."""
        f1 = self.num / self.den
        f2 = other.num / other.den

        return f1 <= f2

    def show_fraction(self):  # methods part
        """Print fraction to screen"""
        print(f"{self.num}/{self.den}")
    

myf = Fraction(3, 5)
myf.show_fraction()
print(myf.__str__())
print(myf)


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)

print((2).__add__(5))  # == 2 + 5 ==  __add__(2, 5)
print(f1 + f2)
print(f1.__add__(f2))

f3 = Fraction(3, 7)
f4 = Fraction(6, 23)
print(f1 == f2)
print(f3.__eq__(f4))

f5 = Fraction(4, 2)
print(f5 + f5)

f6 = Fraction(6, 12)
f6.show_fraction()

f7 = Fraction(2, 4)
f8 = Fraction(1, 4)

print(f7 - f8)
print(f8.__sub__(f7))

print(f3 * f5)

print(f5 / f7)

# The built-in function isinstance(object, type) can be used to determine
# whether an object is of a particular type

print(f2 > f7)
print(f2 >= f7)
print(f3 < f5)
print(f4 <= f1)
