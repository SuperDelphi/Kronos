# Kronos &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/SuperDelphi/Kronos/blob/main/LICENSE)

A light-weight and easy-to-use Python module to calculate the process duration of your code with a complete set of result data on the process.

*Note: Kronos is not available via a standard ``pip`` installation yet.*

### Known issues
• Calculations on short process durations results on inoperable data because of the inaccurate nature of it.

## Getting Started

#### Importing the module only function

```python
from kronos import kalk
```

#### Basic Example

```python
import kronos as k

def add(x, y):
    return x ** y

results = k.kalk(add, x=9999, y=9999)

print(results["total_duration"])
```

Output (in ms): ``5.00146484375``

*Note: The result must (obviously) vary depending on the machine used and the context of execution.*
