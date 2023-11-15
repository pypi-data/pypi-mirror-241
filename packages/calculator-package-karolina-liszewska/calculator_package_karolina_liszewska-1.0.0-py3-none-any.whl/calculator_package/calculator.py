class Calculator:
    """
    A simple calculator that can perform basic arithmetic operations and
    take the nth root of a number. It has a memory to store and manipulate
    the current value.
    """

    def __init__(self):
        """
        Initialize the Calculator with a memory set to 0.
        """
        self.memory = 0  # Initialize memory to 0

    def add(self, num):
        """
        Add the given number to the current value in memory.

        :param num: The number to add.
        """
        self.memory += num

    def subtract(self, num):
        """
        Subtract the given number from the current value in memory.

        :param num: The number to subtract.
        """
        self.memory -= num

    def multiply(self, num):
        """
        Multiply the current value in memory by the given number.

        :param num: The number to multiply by.
        """
        self.memory *= num

    def divide(self, num):
        """
        Divide the current value in memory by the given number.

        :param num: The number to divide by.
        :raises ZeroDivisionError: If num is 0.
        """
        if num == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        else:
            self.memory /= num

    def take_root(self, n):
        """
        Take the nth root of the current value in memory.

        :param n: The root to be taken.
        :raises ValueError: If n is 0 or if the current value is negative and n is even.
        """
        if n == 0:
            raise ValueError("Taking the 0th root is undefined.")
        elif self.memory < 0 and n % 2 == 0:
            raise ValueError("Cannot take an even root of a negative number.")
        else:
            self.memory = self.memory ** (1 / n)

    def reset_memory(self):
        """
        Reset the memory to 0.
        """
        self.memory = 0