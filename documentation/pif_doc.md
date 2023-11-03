# PIFEntry Class Documentation

The `PIFEntry` class represents an entry in the Program Internal Form (PIF), used for storing code and position information.

## Constructor

### `__init__(self, code: int, pos: int)`

The constructor initializes a new `PIFEntry` object with a code and position.

- **Parameters**:
  - `code` (int): The code associated with the entry.
  - `pos` (int): The position of the entry.

## Getter Methods

### `getCode(self) -> int`

Returns the code associated with the `PIFEntry`.

- **Returns**:
  - `int`: The code of the entry.

### `getPos(self) -> int`

Returns the position of the `PIFEntry`.

- **Returns**:
  - `int`: The position of the entry.

## Setter Methods

### `setCode(self, code: int)`

Sets the code of the `PIFEntry` to the specified value.

- **Parameters**:
  - `code` (int): The new code to set.

### `setPos(self, pos: int)`

Sets the position of the `PIFEntry` to the specified value.

- **Parameters**:
  - `pos` (int): The new position to set.

# PIF Class Documentation

The `PIF` class represents the Program Internal Form, used for storing a collection of `PIFEntry` objects.

## Constructor

### `__init__(self)`

The constructor initializes a new `PIF` object with an empty list of elements.

## Add Method

### `add(self, code: int, pos: int)`

Adds a new `PIFEntry` to the `PIF` with the specified code and position.

- **Parameters**:
  - `code` (int): The code to associate with the entry.
  - `pos` (int): The position to associate with the entry.

## Get Method

### `get(self, index: int) -> PIFEntry`

Retrieves a `PIFEntry` from the `PIF` at the specified index.

- **Parameters**:
  - `index` (int): The index of the entry to retrieve.

- **Returns**:
  - `PIFEntry`: The `PIFEntry` object at the specified index.

## String Representation

### `__str__(self) -> str`

Returns a string representation of the `PIF` object, showing its elements.

- **Returns**:
  - `str`: A string representation of the `PIF` object.

