# LexicScanner Class Documentation

The `lexicScanner` class is designed to perform lexical analysis on a source code file. It scans the input code, identifies tokens, and populates the Program Internal Form (PIF) and Symbol Table (ST) accordingly.

## Constructor

### `__init__(self)`

The constructor initializes a `lexicScanner` object. It also initializes the PIF and ST objects, and reads a list of tokens from a file.

- Initializes:
  - `pif` (PIF): A Program Internal Form instance for storing token information.
  - `st` (SymbolTable): A Symbol Table instance for storing symbols.
  - `token_list` (List[str]): A list of valid tokens read from a file.

## Getter Methods

### `getPif(self) -> PIF`

Returns the PIF instance.

- **Returns**:
  - `PIF`: The Program Internal Form instance.

### `getSt(self) -> SymbolTable`

Returns the ST instance.

- **Returns**:
  - `SymbolTable`: The Symbol Table instance.

## File Processing Method

### `process_file(self, input_file: str) -> List[List[str]]`

Reads and processes the content of an input file, splitting it into lines and tokens.

- **Parameters**:
  - `input_file` (str): The path to the input file.

- **Returns**:
  - `List[List[str]]`: A list of lists, where each inner list contains the tokens of a line.

## Token Identification Methods

### `isIdentifier(self, token: str) -> bool`

Checks if a token is an identifier. It verifies that the token contains only letters and numbers and is shorter than 50 characters.

- **Parameters**:
  - `token` (str): The token to check.

- **Returns**:
  - `bool`: `True` if the token is an identifier; otherwise, `False`.

### `isConstant(self, token: str) -> bool`

Checks if a token is a constant. It can be numeric, "Adevarat," or "Fals," or a string enclosed in double quotes.

- **Parameters**:
  - `token` (str): The token to check.

- **Returns**:
  - `bool`: `True` if the token is a constant; otherwise, `False`.

### `isToken(self, token: str) -> bool`

Checks if a token is a valid predefined token from the list of tokens read during initialization.

- **Parameters**:
  - `token` (str): The token to check.

- **Returns**:
  - `bool`: `True` if the token is a predefined token; otherwise, `False`.

## Lexical Analysis Method

### `run(self, file_name: str)`

Processes the input source code file, token by token, and populates the PIF and ST based on the token's type (identifier, constant, or predefined token).

- **Parameters**:
  - `file_name` (str): The path to the source code file.

The `lexicScanner` class performs lexical analysis by identifying tokens and updating the Program Internal Form and Symbol Table accordingly. It can also handle lexical errors.

