class Jar:
    def __init__(self, capacity=12):
        """
        Initialize cookie jar with a given capacity.
        """
        if capacity < 0:
            raise ValueError("Capacity is negative")
        self.__capacity = capacity

        self.__size = 0

    def __str__(self):
        """
        Print emojis representing the number of cookies.
        """
        return "🍪" * self.__size

    def deposit(self, n):
        """
        Deposit a given number of cookies.
        """
        if n < 0:
            raise ValueError("Negative number")
        elif n == 0:
            return

        size_new = self.__size + n
        if size_new > self.__capacity:
            raise ValueError("Exceeded capacity")
        self.__size = size_new

    def withdraw(self, n):
        """
        Withdraw a given number of cookies.
        """
        if n < 0:
            raise ValueError("Negative number")
        elif n == 0:
            return

        size_new = self.__size - n
        if size_new < 0:
            raise ValueError("Empty Jar")
        self.__size = size_new

    @property
    def capacity(self):
        """
        Return jar capacity.
        """
        return self.__capacity

    @property
    def size(self):
        """
        Return number of cookies.
        """
        return self.__size
