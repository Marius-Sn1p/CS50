class Jar:
    def __init__(self, capacity=12, ):

            self.capacity = capacity
            self.size = 0


    def __str__(self):

        return "🍪" * self.size

    def deposit(self, n):

        self.size += n

    def withdraw(self, n):

        self.size -= n

    @property
    def capacity(self):

        return self._capacity

    @property
    def size(self):

        return self._size

    @capacity.setter
    def capacity(self, capacity):

        if capacity < 1:
            raise ValueError

        else:
            self._capacity = capacity

    @size.setter
    def size(self, size):

        if size > self.capacity or size < 0:
            raise ValueError

        else:
            self._size = size

def main():
    jar = Jar()
    print(jar)
    jar.deposit(4)
    print(jar)
    jar.withdraw(2)
    print(jar)
    jar.deposit(10)
    print(jar)
    jar.withdraw(13)
    print(jar)

if __name__ == "__main__":
    main()