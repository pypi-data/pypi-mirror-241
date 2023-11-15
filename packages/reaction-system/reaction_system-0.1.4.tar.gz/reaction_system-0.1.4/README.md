# Reaction System

A Python package for handling Reaction Systems and RsFunctions (partially mapped result functions) with minimization capabilities.

## Overview

Your Package Name provides functionality for working with Reaction Systems and RsFunctions. It includes methods for minimization, mapping, support analysis, and more.

## Features

- **Reaction System Handling:** Create and analyze Reaction Systems.
- **RsFunction Operations:** Perform minimization operations on RsFunctions to convert into ReactionSystems.

## Installation

```bash
pip install your-package-name
```

## Usage

Here's a quick example of using the Reaction System package:

```python
from reaction_system import ReactionSystem, RsFunction

# Create a Reaction System
reaction_system = ReactionSystem(5)
reaction_system.push([1, 2, 3], [], [4, 5])

# Minimize the Reaction System over rank, or degree
rs_rank = reaction_system.minimize_rank()
rs_rank_exact = reaction_system.minimize_rank_exact()
rs_degree = reaction_system.minimize_rank()

# Get the reactions from a reaction system
for reaction in rs_rank.reactions():
  print(reaction, reaction.enabled([1, 2, 3, 4]))

# Create an RsFunction
rs_function = RsFunction(5)
rs_function.add([1, 2], [3, 4])
rs_function.add([1, 3], [2, 4])

# Get a minimum corresponding Reaction System
rs_rank = rs_function.minimize_rank()
rs_rank_exact = rs_function.minimize_rank_exact()
rs_degree = rs_function.minimize_rank()

print(rs_rank)
```

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or want to contribute code, please open an issue or submit a pull request.