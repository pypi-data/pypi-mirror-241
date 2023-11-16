### [TKR - Python Toolkit](https://pypi.org/project/tkr/)
```markdown
## tkr
```

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/toolkitr/tkr/blob/main/LICENSE)
[![Python Versions](https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12%20-blue)](https://www.python.org/downloads/)

```markdown

## Description
```
[TKR](https://github.com/toolkitr/tkr) ```is a Python package that allows for you to save functions to assigned 'Tools' with names, versions, descriptions, etc. Easily keep track of global tools and get a specific tool by name or method.```
```markdown
## Features

- tkr.Tool: Primary class of tkr (tkr.abc.Tool). Protocol tkr.abc._tool.ToolProxy
- tkr.ToolProxy: Protocol method for all Tools, allows users to create their own versions of Tools with ToolProxy.
- tkr.core: tkr's core/parent to methods and processing.

## Installation

You can install `tkr` using pip:
```

```shell
pip install tkr
```

## Usage

To use the `tkr` package, first import it into your Python script:

```python
import tkr
```

Next, you can call the functions and utilities provided by the package. Here's an example:

```python
import tkr

def tkr_tool_test() -> list:
  return tkr.ToolProxy

mytool = tkr.Tool(
  name="mytool",
  version="0.0.1",
  method=tkr_tool_test
)

print(mytool.name, mytool(), mytool.version)
```

For more detailed examples and usage instructions, please refer to the [documentation](https://toolkitr.github.io/tkr).

## Contributing

Contributions are welcome! If you find a bug or want to suggest a new feature, please open an issue or submit a pull request. Make sure to read the [contribution guidelines](https://github.com/toolkitr/tkr/blob/main/CONTRIBUTING.md) before getting started.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/toolkitr/tkr/blob/main/LICENSE) file for details.
