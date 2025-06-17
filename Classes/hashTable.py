class hashtable:
    # Initializes the hash table with a specified size
    def __init__(self, size=15):
        self.size = size
        self.table = [[] for _ in range(size)]  

    # Hashing function to compute the index for a given key
    def hash_function(self, key):
        return hash(key) % self.size

    # Insert a key-value pair into the hash table
    def insert(self, key, value):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  
                return
        self.table[index].append((key, value))  

    # Retrieve a value by using a provided key
    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  

    # Removes value by using a provided key
    def remove(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]  
                return True
        return False  