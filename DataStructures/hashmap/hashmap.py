class HashTable:

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def hash_function(self, key, size):
        return key % size

    def put(self, key, data):
        hash_key = self.hash_function(key, len(self.slots))

        # if the space of hashed key is free, add key & data to slots & data
        if self.slots[hash_key] is None:
            self.slots[hash_key] = key
            self.data[hash_key] = data
        else:
            # if the slot belongs to key - it's fine, rewrite the data
            if self.slots[hash_key] == key:
                self.data[hash_key] = data
            else:
                # if it's occupied by the other key - find new slot
                next_slot = self.hash_function(hash_key + 1, len(self.slots))
                # find empty place or where initial key is stored
                while self.slots[next_slot] is None and self.slots[next_slot] != key:
                    next_slot = self.hash_function(next_slot + 1, len(self.slots))

                # we've found an empty space, we can accommodate now both key and data
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    # otherwise - means we've found the slot of initial key, we can rewrite only data
                    self.data[next_slot] = data  # replace

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.hash_function(position + 1, len(self.slots))
                if position == start_slot:
                    stop = True
        return data


if __name__ == "__main__":
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H.slots)
    print(H.data)


