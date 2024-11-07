#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Rational:
    MAX_DIGITS = 100  # Maximum digits for numerator and denominator

    def __init__(self, a: int = 0, b: int = 1, size: int = 100):
        if b == 0:
            raise ValueError("Denominator cannot be zero")
        self.size = min(size, self.MAX_DIGITS)
        self.numerator = self._int_to_digits(abs(a))
        self.denominator = self._int_to_digits(abs(b))
        self.sign = -1 if (a < 0) ^ (b < 0) else 1
        self._reduce()

    # Convert integer to digits list
    def _int_to_digits(self, value: int) -> list:
        digits = [0] * self.size
        idx = 0
        while value > 0 and idx < self.size:
            digits[idx] = value % 10
            value = value // 10
            idx += 1
        return digits

    # Convert digits list to integer
    def _digits_to_int(self, digits: list) -> int:
        value = 0
        for idx in reversed(range(self.size)):
            value = value * 10 + digits[idx]
        return value

    # Compute GCD using integers
    def _gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    # Reduce the fraction
    def _reduce(self):
        num = self._digits_to_int(self.numerator)
        denom = self._digits_to_int(self.denominator)
        if num == 0:
            self.denominator = [1] + [0]*(self.size-1)
            return
        gcd = self._gcd(num, denom)
        num //= gcd
        denom //= gcd
        self.numerator = self._int_to_digits(num)
        self.denominator = self._int_to_digits(denom)

    # String representation
    def __str__(self):
        num = self._digits_to_int(self.numerator)
        denom = self._digits_to_int(self.denominator)
        sign = '-' if self.sign < 0 else ''
        return f"{sign}{num} / {denom}"

    def __repr__(self):
        return self.__str__()

    # Addition
    def __add__(self, other):
        if not isinstance(other, Rational):
            raise ValueError("Can only add Rational instances")
        num1 = self.sign * self._digits_to_int(self.numerator)
        denom1 = self._digits_to_int(self.denominator)
        num2 = other.sign * other._digits_to_int(other.numerator)
        denom2 = other._digits_to_int(other.denominator)
        new_num = num1 * denom2 + num2 * denom1
        new_den = denom1 * denom2
        return Rational(new_num, new_den, self.size)

    # Subtraction
    def __sub__(self, other):
        if not isinstance(other, Rational):
            raise ValueError("Can only subtract Rational instances")
        num1 = self.sign * self._digits_to_int(self.numerator)
        denom1 = self._digits_to_int(self.denominator)
        num2 = other.sign * other._digits_to_int(other.numerator)
        denom2 = other._digits_to_int(other.denominator)
        new_num = num1 * denom2 - num2 * denom1
        new_den = denom1 * denom2
        return Rational(new_num, new_den, self.size)

    # Multiplication
    def __mul__(self, other):
        if not isinstance(other, Rational):
            raise ValueError("Can only multiply Rational instances")
        num1 = self.sign * self._digits_to_int(self.numerator)
        denom1 = self._digits_to_int(self.denominator)
        num2 = other.sign * other._digits_to_int(other.numerator)
        denom2 = other._digits_to_int(other.denominator)
        new_num = num1 * num2
        new_den = denom1 * denom2
        return Rational(new_num, new_den, self.size)

    # True division
    def __truediv__(self, other):
        if not isinstance(other, Rational):
            raise ValueError("Can only divide by Rational instances")
        num1 = self.sign * self._digits_to_int(self.numerator)
        denom1 = self._digits_to_int(self.denominator)
        num2 = other.sign * other._digits_to_int(other.numerator)
        denom2 = other._digits_to_int(other.denominator)
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        new_num = num1 * denom2
        new_den = denom1 * num2
        if new_den < 0:
            new_den = -new_den
            new_num = -new_num
        return Rational(new_num, new_den, self.size)

    # Equality
    def __eq__(self, other):
        if not isinstance(other, Rational):
            return False
        return (self.sign * self._digits_to_int(self.numerator) == other.sign * other._digits_to_int(other.numerator) and
                self._digits_to_int(self.denominator) == other._digits_to_int(other.denominator))

    # Less than
    def __lt__(self, other):
        if not isinstance(other, Rational):
            return False
        return (self.sign * self._digits_to_int(self.numerator) * other._digits_to_int(other.denominator) <
                other.sign * other._digits_to_int(other.numerator) * self._digits_to_int(self.denominator))

    # Other comparison operators
    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    # Float conversion
    def __float__(self):
        num = self.sign * self._digits_to_int(self.numerator)
        denom = self._digits_to_int(self.denominator)
        return num / denom if denom != 0 else float('inf')

    # Boolean conversion
    def __bool__(self):
        return self._digits_to_int(self.numerator) != 0


# Example usage
if __name__ == '__main__':
    r1 = Rational(123, 456, 100)
    print(f"r1 = {r1}")
    r2 = Rational(-789, 1011, 100)
    print(f"r2 = {r2}")
    print(f"r1 + r2 = {r1 + r2}")
    print(f"r1 - r2 = {r1 - r2}")
    print(f"r1 * r2 = {r1 * r2}")
    print(f"r1 / r2 = {r1 / r2}")
    print(f"r1 == r2: {r1 == r2}")
    print(f"r1 < r2: {r1 < r2}")
    print(f"r1 > r2: {r1 > r2}")