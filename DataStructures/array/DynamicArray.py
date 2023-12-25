class DynamicArray:

    def __init__(self, capacity: int):
        try:
            capacity = int(capacity)
        except Exception as e:
            raise ValueError("Array capacity should have integer type")
        if capacity <= 0:
            raise ValueError("Array capacity can't have a negative value")
        self.capacity = capacity
        self.array = [0] * self.capacity
        self.length = 0

    def _validate_value(self, n: int):
        try:
            int(n)
        except Exception as e:
            raise ValueError("Value should be integer type")

    def _validate_index(self, i: int):
        try:
            int(i)
        except Exception as e:
            raise ValueError("Array index should be integer type")
        if i < 0 or i >= self.capacity:
            raise ValueError(f"Array index should be in bounds of array 0-{self.capacity - 1}")

    def get(self, i: int) -> int:
        self._validate_index(i)
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self._validate_index(i)
        self._validate_value(n)
        self.array[i] = n

    def pushback(self, n: int) -> None:
        self._validate_value(n)
        if self.capacity == self.length:
            self.resize()

        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length == 0:
            raise Exception("Array is empty")
        self.length -= 1
        return self.array[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [0] * self.capacity
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity

    # Insert n at i-th index
    def insert(self, i, n):
        self._validate_value(i)
        self._validate_value(n)
        # make sure we have enough room for +1 element
        if self.capacity == self.length + 1:
            self.resize()

        # shift starting from i, all elements further by 1 (i.e. i -> i+1)
        for j in range(self.length-1, i-1, -1):
            self.array[j+1] = self.array[j]

        # now we can rewrite the element on the i-th position with value n
        self.array[i] = n


    def print(self):
        for i in range(self.length):
            print(self.array[i])
        print()
