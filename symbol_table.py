class SymbolTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def insert(self, key):
        index = self.hash(key)
        for elem in self.table[index]:
            if elem == key:
                return [index, self.table[index].index(elem)]
        self.table[index].append(key)
        return [index, self.table[index].index(key)]

    def get(self, key):
        index = self.hash(key)
        for elem in self.table[index]:
            if elem == key:
                return [index, self.table[index].index(key)]
        return None

    def display(self):
        for index, slot in enumerate(self.table):
            print(f"Hash {index}:")
            for elem in slot:
                print(f"   {elem} at index: {self.table[index].index(elem)}")


if __name__ == "__main__":
    # Example usage
    hash_table = SymbolTable(2)

    hash_table.insert("apple")
    hash_table.insert("banana")
    hash_table.insert("cherry")

    print("Initial Hash Table:")
    hash_table.display()

    print("Get value for 'apple':", hash_table.get("apple"))
    print("Get value for 'banana':", hash_table.get("banana"))

    print("After removing 'banana':")
    hash_table.display()
