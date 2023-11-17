# oculist

Statically typed, purely functional lenses for Python.

# Features


# Quickstart

```python
from dataclasses import dataclass

from oculist import Lens


@dataclass(frozen=True)
def Address:
    street: Lens[str] = Lens()


@dataclass(frozen=True)
def User:
    name: Lens[str] = Lens()  # 'Lens' is a descriptor
    address: Lens[Address] = Lens()


bob = User('bob', Address("Some st."))

alice = (
    bob
    > User.name << 'alice'  # Define transformations using << and apply using >
    | User.address * Address.street << 'Other st.' # Compose transformations with | and chain lenses with *
)

assert bob.name == 'bob' and alice.name == 'alice'  # original target is left untouched
```

# Concepts

## Lenses, Attributes and Setters
## Special Lenses

### List
### Tuple
### Dict
### Set