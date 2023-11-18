<div id="header">
  <img src="https://media.discordapp.net/attachments/1171675700055506989/1174869224750059540/tkr.social.preview.png?ex=6569293b&is=6556b43b&hm=2671fa13030c24a58ace7738fe2c99ee5df4297efe0785361a4c67eeabfc20b3&=&width=997&height=499" width="400"/>
</div>

# [TKR - Python Toolkit](https://pypi.org/project/tkr/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/toolkitr/tkr/blob/main/LICENSE)
[![Python Versions](https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12%20-blue)](https://www.python.org/downloads/)

```Allow python developers to easily manage classes, methods, and more!```
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></a></p>

## Installing
```shell
# Linux/macOS
python3 -m pip install -U tkr

# Windows
py -3 -m pip install -U tkr
```
Development Version:
```shell
$ git clone https://github.com/toolkitr/tkr
$ cd tkr
```

# Simple Example
```python
import tkr

def tkr_tool_test() -> list:
  return tkr.ToolProxy

mytool = tkr.Tool(
  name="mytool",
  description="Simple tool example",
  version="0.0.1",
  method=tkr_tool_test
)

print(mytool.name, mytool(), mytool.version)

# Get tool by name
print(tkr.byname("mytool").id)
```

# Links
- [Github](https://github.com/toolkitr/tkr)
- [PyPi](https://pypi.org/project/tkr)
- [Issues](https://github.com/toolkitr/tkr/issues)
- [Discussions](https://github.com/toolkitr/tkr/discussions)