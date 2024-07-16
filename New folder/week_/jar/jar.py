class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        if self._capacity < 0:
            raise ValueError ("capacity error")
        self._size = 0

    def __str__(self):
        return self._size * ("🍪")

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Deposit error")
        self.size = self.size + n

    def withdraw(self, n):
        if  n > self._size:
            raise ValueError ("Withdraw error")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError ("@capacity.setter error")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError ("@size.setter error")
        self._size = size

def main():
    jar = Jar()
    print(jar)
    jar.deposit(1)
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(2)
    print(jar)


if __name__ == "__main__":
    main()
