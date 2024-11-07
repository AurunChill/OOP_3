#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Rational:
    def __init__(self, a: int = 0, b: int = 1):
        if b == 0:
            raise ValueError()
        self.__numerator = abs(int(a))
        self.__denominator = abs(int(b))
        self.__reduce()

    # Сокращение дроби
    def __reduce(self):
        # Функция для нахождения нибольшего общего делителя
        def gcd(a: int, b: int):
            if a == 0:
                return b
            elif b == 0:
                return a
            elif a >= b:
                return gcd(a % b, b)
            else:
                return gcd(a, b % a)

        sign = 1
        if (self.__numerator > 0 and self.__denominator < 0) or \
                (self.__numerator < 0 and self.__denominator > 0):
            sign = -1

        a, b = abs(self.__numerator) , abs(self.__denominator)
        c = gcd(a, b)

        self.__numerator = sign * (a // c)
        self.__denominator = b // c

    def __clone(self):
        return Rational(self.__numerator, self.__denominator)

    @property
    def numerator(self) -> int:
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        self.__numerator = int(value)
        self.__reduce()

    @property
    def denominator(self) -> int:
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        value = int(value)
        if value == 0:
            raise ValueError('Illegal value of the denominator')
        self.__denominator = value
        self.__reduce()

    def __str__(self):
        return f'{self.__numerator} / {self.__denominator}'

    def __repr__(self):
        return self.__str__()

    def __float__(self):
        return self.__numerator / self.__denominator

    def __bool__(self):
        return self.__numerator != 0

    def __iadd__(self, other):
        if isinstance(other, Rational):
            a = self.numerator * other.denominator / self.denominator * other.numerator
            b = self.denominator * other.denominator

            self.__numerator, self.__denominator = a, b
            self.__reduce()
            return self
        else:
            raise ValueError('Illegal type of the argument')

    def __add__(self, other):
        return self.__clone().__iadd__(other)

    def __isub__(self, other):
        if isinstance(other, Rational):
            a = self.numerator * other.denominator - self.denominator * other.numerator
            b = self.denominator * other.denominator
            self.__numerator, self.__denominator = a, b
            self.__reduce()
            return self
        else:
            raise ValueError('Illegal tpe of the argument')

    def __sub__(self, other):
        return self.__clone().__isub__(other)

    def __imul__(self, other):
        if isinstance(other, Rational):
            a = self.numerator * other.numerator
            b = self.denominator * other.denominator

            self.__numerator, self.__denominator = a, b
            self.__reduce()
            return self
        else:
            raise ValueError('Illegal type of the argument')

    def __mul__(self, other):
        return self.__clone().__imul__(other)

    def __truediv__(self, other):
        if isinstance(other, Rational):
            a = self.numerator * other.denominator
            b = self.denominator * other.numerator

            if b == 0:
                raise ValueError('Illegal value of the denominator')
            self.__numerator, self.__denominator = a, b
            self.__reduce()
            return self
        else:
            raise ValueError('Illegal type of the argument')

    def __eq__(self, other):
        if isinstance(other, Rational):
            return (self.numerator == other.numerator) and (self.denominator == other.denominator)

    def __ne__(self, other):
        if isinstance(other, Rational):
            return not self.__eq__(other)
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Rational):
            return self.__float__() > other.__float__()
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rational):
            return self.__float__() < other.__float__()
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Rational):
            return not self.__lt__(other)
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Rational):
            return not self.__gt__(other)
        else:
            return False


if __name__ == '__main__':
    r1 = Rational(3, 4)
    print(f"r1 = {r1}")
    r2 = Rational(5, 6)
    print(f"r2 = {r2}")
    print(f"r1 + r2 = {r1 + r2}")
    print(f"r1 - r2 = {r1 - r2}")
    print(f"r1 * r2 = {r1 * r2}")
    print(f"r1 / r2 = {r1 / r2}")
    print(f"r1 == r2: {r1 == r2}")
    print(f"r1 != r2: {r1 != r2}")
    print(f"r1 > r2: {r1 > r2}")
    print(f"r1 < r2: {r1 < r2}")
    print(f"r1 >= r2: {r1 >= r2}")
    print(f"r1 <= r2: {r1 <= r2}")