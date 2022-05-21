class hash_table():
    def __init__(self, size=1024):
        self.size = size
        self.data = [None]*self.size

    def __str__(self):
        return str(self.__dict__)

    def _hash(self, key):
        """ Method to hash the key and return the index of the array 
            Input: key
            Output: index of the array
        """
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % self.size
        return hash

    def get(self, key):
        """ Method to get the value of the key 
            Input: key
            Output: value of the key
        """
        hash = self._hash(key)
        if self.data[hash]:
            for i in range(len(self.data[hash])):
                if self.data[hash][i][0] == key:
                    return self.data[hash][i][1]
        return None

    def set(self, key, value):
        """ Method to set a key and value in the hash table 
            Input: key and value
            Output: None
        """
        hash = self._hash(key)
        if not self.data[hash]:
            self.data[hash] = [[key, value]]
        else:
            self.data[hash].append([key, value])
        print(self.data)

    def keys(self):
        """ Method to return all the keys
            Input: None
            Output: list of keys
        """
        keys_array = []
        for i in range(self.size):
            if self.data[i]:
                if len(self.data[i]) > 1:
                    for j in range(len(self.data[i])):
                        keys_array.append(self.data[i][j][0])
                else:
                    keys_array.append(self.data[i][0][0])
        return keys_array

    def values(self):
        """Method to return all the values
            Input: None
            Output: list of values
        """
        values_array = []
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    values_array.append(self.data[i][j][1])
        return values_array

    def contains(self, key):
        """Method to check if the key is present in the hash table
            Input: key
            Output: True or False
        """
        hash = self._hash(key)
        if self.data[hash]:
            for i in range(len(self.data[hash])):
                if self.data[hash][i][0] == key:
                    return True
        return False
    

if __name__ == '__main__':
    new_hash = hash_table(2)
    print(new_hash)
    #{'size': 2, 'data': [None, None]}

    new_hash.set('one', 1)
    new_hash.set('two', 2)
    new_hash.set('three', 3)
    new_hash.set('four', 4)
    new_hash.set('five', 5)
    print(new_hash)
    #{'size': 2, 'data': [[['one', 1], ['five', 5]], [['two', 2], ['three', 3], ['four', 4]]]}

    print(new_hash.get('one'))
    # 1

    print(new_hash.keys())
    #['one', 'five', 'two', 'three', 'four']
    print(new_hash.values())
    #[1, 5, 2, 3, 4]

    print(new_hash.contains('one'))
    # True
    print(new_hash.contains('six'))
    # False

    new_hash.set('one', 1)
    new_hash.set('eno', 2)
    print(new_hash)
    
    # print(hash_table._hash('Cat'))
    ht=hash_table(2)
    ht._hash('one')
    print(ht)