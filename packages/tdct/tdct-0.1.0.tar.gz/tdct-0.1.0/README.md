# timing_decorator

`timing_decorator` is a Python module that provides a decorator for measuring the execution time of functions.

## Installation

You can install the package using pip:

```bash
pip install timing_decorator
```

## Usage

```python
from timing_decorator.decorator import timing_decorator
import time

@timing_decorator
def example_function():
    time.sleep(3)
    return True

result = example_function()
print(result)
```

The `timing_decorator` will print the execution time of the decorated function.

## Contributing

If you want to contribute to this project, feel free to submit a pull request.

## License

This project is licensed under the MIT License.
