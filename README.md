![Kronos logo](https://raw.githubusercontent.com/SuperDelphi/Kronos/main/logo.png)

# Kronos &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/SuperDelphi/Kronos/blob/main/LICENSE)

A light-weight and easy-to-use Python module to calculate the process duration of your code with a complete set of result data on the process.

**Please be aware that this module is for educational purpose only. There are better ones to get the job done :)**

*Note: Kronos is not available via a standard ``pip`` installation yet.*

### Known issues
• Calculations on short process durations results on inoperable data because of the inaccurate nature of it.

## Getting Started

The only file you need is ``kronos.py``, located at the root of the ``master`` branch.

#### Importing the module only function

```python
from kronos import kalk
```

#### Basic Example

```python
# Kronos module import
import kronos as k

# The function whose execution time is to be measured
def pow(x, y):
    return x ** y

# Retrieval of the results
results = k.kalk(pow, x=9999, y=9999)

# Display of the total duration
print(results["total_duration"])
```

Output (in ms): ``5.00146484375``

*Note: The result must (obviously) vary depending on the machine used and the context of execution.*
