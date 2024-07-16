class Jar:
    def __init__(self, capacity=12):
        ###capacity = int(input("capacity: "))
        if not capacity > 0:
            raise ValueError ("wrong capacity")
        self._capacity = capacity
        self.size = 0
    def __str__(self):
        return self.size * ("🍪")

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

jar = Jar()
print(jar)
