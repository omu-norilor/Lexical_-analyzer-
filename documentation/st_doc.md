# SymbolTable Class Documentation

The `SymbolTable` class is a simple implementation of a hash table data structure designed to store and manage a collection of symbols (keys) efficiently. It uses a basic hash function to determine the index where each symbol should be stored. If multiple symbols hash to the same index, they are placed in a list at that index. This class provides methods for inserting, retrieving, and displaying symbols stored in the table.

## Class Constructor

### `__init__(self, size: int)`

The constructor initializes a new instance of the `SymbolTable` class with a specified size. This size determines the number of slots or buckets in the hash table.

- **Parameters**:
  - `size` (int): The number of slots in the hash table.

## Hashing Method

### `hash(self, key: str) -> int`

This method calculates the hash value for a given key. It uses a simple algorithm that sums the ASCII values of each character in the key and then takes the modulo of the sum with the table size to determine the index where the key should be stored.

- **Parameters**:
  - `key` (str): The symbol to be hashed.

- **Returns**:
  - `int`: The index in the hash table where the key should be stored.

## Insertion Method

### `insert(self, key: str) -> List[int]`

The `insert` method adds a symbol to the hash table. If the symbol already exists in the hash table, it returns the index and position of the symbol in the list. If the symbol is not present, it inserts the symbol and returns the index and position where it was added.

- **Parameters**:
  - `key` (str): The symbol to be inserted.

- **Returns**:
  - `List[int]`: A list containing two integers - the index in the hash table and the position in the list where the key is located.

## Retrieval Method

### `get(self, key: str) -> List[int] or None`

The `get` method searches for a symbol in the hash table and returns its index and position if it exists. If the symbol is not found, it returns `None`.

- **Parameters**:
  - `key` (str): The symbol to be retrieved.

- **Returns**:
  - `List[int]` if the symbol is found: A list containing two integers - the index in the hash table and the position in the list where the key is located.
  - `None` if the symbol is not found.

## Display Method

### `display(self)`

The `display` method is used to print the contents of the hash table. It lists each slot (hash index) along with the symbols stored at that index.

- **Output**: Prints the hash table with slot indices and the symbols in each slot.

## Example Usage

```python
# Create a SymbolTable instance with a size of 10
symbol_table = SymbolTable(10)

# Insert symbols into the table
symbol_table.insert("apple")
symbol_table.insert("banana")
symbol_table.insert("cherry")

# Retrieve the index and position of a symbol
index_and_position = symbol_table.get("banana")
print("Index and Position:", index_and_position)

# Display the contents of the table
symbol_table.display()
