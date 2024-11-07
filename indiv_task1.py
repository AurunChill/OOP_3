#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def _is_number(value) -> bool:
    """
    Checks if the given value can be converted to a float.

    :param value: The value to check
    :return: True if the value is a number, False otherwise
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


class Pair:
    def __init__(self, first: float = None, second: float = None):
        """
        Initializes a Pair instance with two numbers.

        :param first: The first number of the pair
        :param second: The second number of the pair
        """
        self.first = first
        self.second = second

    def read(self):
        """
        Reads two numbers from user input and assigns them to the pair.
        Raises a ValueError if the input is not a number or if first >= second.
        """
        first_input = input('Enter first argument: ')
        if not _is_number(first_input):
            raise ValueError('Argument must be number!')
        second_input = input('Enter second argument: ')
        if not _is_number(second_input):
            raise ValueError('Argument must be number!')
        first_input, second_input = float(first_input), float(second_input)
        if first_input >= second_input:
            raise ValueError('First argument must be less than the second one!')

        self.first = first_input
        self.second = second_input

    def __str__(self):
        """
        Returns a string representation of the range.
        """
        return f'Range: ({self.first}:{self.second})'

    def __contains__(self, number: int | float) -> bool:
        """
        Enables use of 'in' keyword to check if a number is within the range.

        :param number: The number to check
        :return: True if the number is within the range, False otherwise
        """
        return self.first < number < self.second

    def __lt__(self, other):
        """
        Defines the less than comparison based on the first value.
        """
        if isinstance(other, Pair):
            return self.first < other.first
        return NotImplemented

    def __le__(self, other):
        """
        Defines the less than or equal comparison based on the first value.
        """
        if isinstance(other, Pair):
            return self.first <= other.first
        return NotImplemented

    def __eq__(self, other):
        """
        Defines equality comparison based on both first and second values.
        """
        if isinstance(other, Pair):
            return self.first == other.first and self.second == other.second
        return NotImplemented

    def __ne__(self, other):
        """
        Defines non-equality comparison based on both first and second values.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Defines the greater than comparison based on the first value.
        """
        if isinstance(other, Pair):
            return self.first > other.first
        return NotImplemented

    def __ge__(self, other):
        """
        Defines the greater than or equal comparison based on the first value.
        """
        if isinstance(other, Pair):
            return self.first >= other.first
        return NotImplemented


def make_pair(first: int | float, second: int | float) -> Pair:
    """
    Creates a Pair instance with the given numbers.

    :param first: The first number
    :param second: The second number
    :return: A Pair instance
    :raises ValueError: If arguments are not numbers or first >= second
    """
    if not isinstance(first, (int, float)) or not isinstance(second, (int, float)):
        raise ValueError('Arguments must be numbers!')
    if first >= second:
        raise ValueError('First argument must be less than the second argument!')
    return Pair(first=first, second=second)


if __name__ == '__main__':
    # Create initial pair and display
    pair1 = make_pair(5, 10)
    print("Pair1:", pair1)

    # Read new values for pair1
    try:
        pair1.read()
        print("Updated Pair1:", pair1)
    except ValueError as e:
        print("Error during read:", e)

    # Create another pair for comparison
    try:
        pair2 = make_pair(3, 8)
        print("Pair2:", pair2)
    except ValueError as e:
        print("Error creating Pair2:", e)

    # Demonstrate comparison operators
    print(f"Is Pair1 < Pair2? {pair1 < pair2}")
    print(f"Is Pair1 <= Pair2? {pair1 <= pair2}")
    print(f"Is Pair1 == Pair2? {pair1 == pair2}")
    print(f"Is Pair1 != Pair2? {pair1 != pair2}")
    print(f"Is Pair1 > Pair2? {pair1 > pair2}")
    print(f"Is Pair1 >= Pair2? {pair1 >= pair2}")

    # Demonstrate containment
    test_numbers = [7, 4, 10]
    for number in test_numbers:
        print(f"Is {number} in Pair1? {'Yes' if number in pair1 else 'No'}")

    # Demonstrate string representation
    print("String representation of Pair1:", str(pair1))
    print("String representation of Pair2:", str(pair2))