# Transition Class Documentation

The `Transition` class represents a transition in a finite state machine. It has three attributes: `fromState`, `toState`, and `symbol`. The `fromState` attribute specifies the state from which the transition originates, the `toState` attribute specifies the state to which the transition leads, and the `symbol` attribute specifies the symbol that triggers the transition.


## Class Constructor

### `__init__(self, fromState: str, toState: str, symbol: str)`

The constructor initializes a new instance of the `Transition` class with the specified `fromState`, `toState`, and `symbol` attributes.

- **Parameters**:
  - `fromState` (str): The state from which the transition originates.
  - `toState` (str): The state to which the transition leads.
  - `symbol` (str): The symbol that triggers the transition.

## Getter Methods

### `getFromState(self) -> str`

Returns the fromState associated with the `Transition`.

- **Returns**:
  - `str`: The fromState of the transition.

### `getToState(self) -> str`

Returns the ToState of the `Transition`.

- **Returns**:
  - `str`: The ToState of the transition.

### `getSymbol(self) -> str`

Returns the symbol of the `Transition`.

- **Returns**:
  - `str`: The symbol of the transition.

## Setter Methods

### `setFromState(self, fromState: str)`

Sets the fromState of the `Transition` to the specified value.

- **Parameters**:
  - `fromState` (str): The new fromState to set.

### `setToState(self, toState: str)`

Sets the toState of the `Transition` to the specified value.

- **Parameters**:
  - `toState` (str): The new toState to set.

### `setSymbol(self, symbol: str)`

Sets the symbol of the `Transition` to the specified value.

- **Parameters**:
  - `symbol` (str): The new symbol to set.