# Dagwood 

[![PyPI version](https://badge.fury.io/py/dagwood.svg)](https://badge.fury.io/py/dagwood)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<img src="dagwood.png" alt="Dagwood Bumstead" width="200"/>

<br/>

Dagwood is a Swiss Army knife for Python, a collection of small utilities that I find myself using over and over again. It's named after [Dagwood Bumstead](https://en.wikipedia.org/wiki/Dagwood_Bumstead), the sandwich-loving husband of [Blondie](https://en.wikipedia.org/wiki/Blondie_(comic_strip)) in the eponymous comic strip.

Why "Dagwood"? Because a.) I like sandwiches, and b.) the name was available on PyPI.

To install Dagwood, run:

```
pip install dagwood
```

## Available Utilities

### Logging

To quickly set up a logger:

```python
import dagwood
logger = dagwood.assemble()
```

This will create a logger with default settings: log level set to `INFO` and log messages formatted as `'%(asctime)s - %(levelname)s - %(message)s'`. Logs will be written to a folder named `logs`.

You can customize the log folder, log file name, log level, and log format by passing optional parameters to `assemble`.

- `folder_name`: The name of the folder to store log files (default: `'logs'`)
- `file_name`: The name of the log file (default: `None`, which generates a log file with a timestamp)
- `level`: The log level (default: `logging.INFO`)
- `format`: The log format (default: `'%(asctime)s - %(levelname)s - %(message)s'`)

```python
logger = dagwood.assemble(folder_name='my_logs', file_name='app.log', level=logging.DEBUG, format='%(levelname)s - %(message)s')
```

### HTTP Codes

An easy way to check the meaning of an HTTP status code:

```python
from dagwood import http_codes

# Example of interpreting an HTTP code
CODE = 500
response = http_codes.interpret(CODE)

print(response.message)  # 'Internal Server Error'
print(response.explanation)  # 'The server has encountered a situation it does not know how to handle.'

# Checking the type of the response
types = http_codes.get_enums()
if response.type == types.SERVER_ERROR:
    # Handle server error
    pass
```

You can also retrieve the different types of HTTP responses:
```python
types = http_codes.get_enums()
print(types)  # ['Informational', 'Success', 'Redirection', 'Client Error', 'Server Error']
```

## Contributing

Feel free to open an issue or submit a pull request.

To publish a new version to PyPI:
```bash
pip install twine # if you don't have it already
python setup.py sdist bdist_wheel # build the package
twine upload dist/* # upload to PyPI
```

## Development

### Running Tests

The test suite can be run using Python's built-in `unittest` framework.

Navigate to the `tests` directory and run:

```
python -m unittest test_dagwood.py
```

Or, if you're in the root directory:

```
python -m unittest tests/test_dagwood.py
```
