# Prettier
**A simple *JSON* syntax highlighter implemented in python.**

## Usage

```python
import prettier

print(prettier.pretty({"string" : "hello world", "list" : ["list", 3, None]}))
```

## Features
- **Data types**: This module can pretty print list, dictionary, numbers, strings, None value.
- **Support nested list and dictionary**: This module uses recursion to highlight object.

## Requirements
- **colorama**: *colorama* helps to get terminal colors

### What I Have Learned
- Recursion
- Python Data Types
