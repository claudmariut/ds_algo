"""Implementation of Map ADT."""


class HashTable:
    def __init__(self):
        self.size = 11
        self.keys = [None] * self.size
        self.data = [None] * self.size

    def hashFunction(self, key, size):
        return key % size

    def rehashFunction(self, oldhash, size):
        return (oldhash + 1) % size

    def put(self, key, data):
        """Given key/value pair, insert in hash table, or replace data."""
        hashValue = self.hashFunction(key, self.size)

        if self.keys[hashValue] == None:
            self.keys[hashValue] = key
            self.data[hashValue] = data
        else:
            if self.keys[hashValue] == key:
                # If the key already exist, replace the data.
                self.data[hashValue] = data
            else:
                newhashvalue = self.rehashFunction(hashValue, self.size)
                while self.keys[newhashvalue] != None \
                    and self.keys[newhashvalue] != key:
                    newhashvalue = self.rehashFunction(newhashvalue, self.size)

                if self.keys[newhashvalue] == None:
                    self.keys[newhashvalue] = key
                    self.data[newhashvalue] = data
                else:
                    # Replace with new data.
                    self.data[newhashvalue] = data

    def get(self, key):
        """Return data value of the key if present."""
        hashvalue = self.hashFunction(key, self.size)

        data = None
        found = False
        stop = False
        position = hashvalue

        while self.keys[position] != None and not found and not stop:
            if self.keys[position] == key:
                found = True
                data = self.data[position]

            else:
                position = self.rehashFunction(position, self.size)
                if position == hashvalue:
                    stop = True

        return data

    def __getitem__(self, key):
        """Overload method to access the value of the key with []."""
        return self.get(key)

    def __setitem__(self, key, data):
        """Overload method to set item with h[key] = data"""
        self.put(key, data)

    def __delitem__(self, key):
        """Delete data from key, and reset key to None"""
        hashvalue = self.hashFunction(key, self.size)

        data = None
        found = False
        stop = False
        position = hashvalue

        while self.keys[position] != None and not found and not stop:
            if self.keys[position] == key:
                found = True
                data = self.data[position]

            else:
                position = self.rehashFunction(position, self.size)
                if position == hashvalue:
                    stop = True

        if data != None:
            self.keys[position] = None
            self.data[position] = None

    def __len__(self):
        return self.size

    def __contains__(self, data):
        return data in self.data
