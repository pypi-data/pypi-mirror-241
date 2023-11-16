import asyncio
import inspect
from ._tool import ToolProxy

abc_types: tuple = (
  'TOOL.TKR.PROXY',
  'TOOL.TKR.CLASSIC'
)

VERSION: str = abc_types[1]

class Tool(ToolProxy):
  slots: tuple = ('name', 'version', 'description', 'method', '__name__', '__version__', '__description__', '__method__', 'type', '__type__')

  def __init__(self, method: object, name: str='Tool.DefaultName', version: str='Tool.NoVersion', description: str='Tool.Description', *args, **kwargs) -> None:
    self.name: str = name
    self.__name__: str = self.name
    self.version: str = version
    self.__version__: str = self.version
    self.description: str = description
    self.__description__: str = self.description
    self.desc: str = self.description
    self.__desc__: str = self.description
    self.method: str = method
    self.__method__: str = self.method
    self.func: str = self.method
    self.__func__: str = self.method
    self.type: str = VERSION
    self.__type__: str = self.type

  def run(self, *args, **kwargs):
    if inspect.iscoroutinefunction(self.method): asyncio.run(self.method(*args, **kwargs))
    else: self.method(*args, **kwargs)

  def info(self, *args, **kwargs) -> dict:
    return {
      'name': self.name,
      'version': self.version,
      'description': self.description,
      'method': self.method,
      'type': self.type
    }

  def __dict__(self, *args, **kwargs) -> dict:
    return self.info()

  def __tuple__(self, *args, **kwargs) -> tuple:
    return (self.name, self.version, self.description, self.method, self.type)

  def __list__(self, *args, **kwargs) -> list:
    return [self.name, self.version, self.description, self.method, self.type]

  def __repr__(self, *args, **kwargs) -> str:
    return f'<Tool name={self.name} version={self.version} description={self.description} method={self.method} type={self.type}>'

  def __str__(self, *args, **kwargs) -> str:
    return self.__repr__()

  def __call__(self, *args, **kwargs) -> object:
    return self.method(*args, **kwargs)

  def __int__(self, *args, **kwargs) -> int:
    return int(str(self.version).replace('.', ''))

  def __eq__(self, other, *args, **kwargs) -> bool:
    return self.version == other.version, self.name == other.name, self.description == other.description, self.method == other.method, self.type == other.type

  def __ne__(self, other, *args, **kwargs) -> bool:
    return self.version != other.version, self.name != other.name, self.description != other.description, self.method != other.method, self.type != other.type