class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int):
            raise ValueError("input was not int")
        if capacity < 0:
            raise ValueError("input was not positive")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "c" * self._size

    def deposit(self, n):
        if not isinstance(n, int):
            raise ValueError("input was not int")
        if n < 0:
            raise ValueError("input was not positive")
        if self._size + n > self._capacity:
            raise ValueError("exceeds capacity")
        self._size += n
            
    def withdraw(self, n):
        if not isinstance(n, int):
            raise ValueError("input was not int")
        if n < 0:
            raise ValueError("input was not positive")
        if self._size - n < 0 :
            raise ValueError("no such amount")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    
