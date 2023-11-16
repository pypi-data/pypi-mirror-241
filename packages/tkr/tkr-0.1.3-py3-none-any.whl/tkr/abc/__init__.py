from ._tool import ToolProxy

__all__ = (
    'ToolProxy',
    'Tool'
)

class Tool(ToolProxy):
  slots = ('name', 'version', 'description', 'method', '__name__', '__version__', '__description__', '__method__')
  def __init__(self, name: str, version: str, description: str, method: object, *args, **kwargs) -> None:
    self.name = name
    self.__name__ = self.name
    self.version = version
    self.__version__ = self.version
    self.description = description
    self.__description__ = self.description
    self.method = method
    self.__method__ = self.method

  def info(self, *args, **kwargs) -> dict:
    return {
      'name': self.name,
      'version': self.version,
      'description': self.description,
      'method': self.method,
    }

  def __dict__(self, *args, **kwargs) -> dict:
    return self.info()

  def __tuple__(self, *args, **kwargs) -> tuple:
    return (self.name, self.version, self.description, self.method)

  def __list__(self, *args, **kwargs) -> list:
    return [self.name, self.version, self.description, self.method]

  def __repr__(self, *args, **kwargs) -> str:
    return f'<Tool name={self.name} version={self.version} description={self.description} method={self.method}>'

  def __str__(self, *args, **kwargs) -> str:
    return self.__repr__()

  def __call__(self, *args, **kwargs) -> object:
    return self.method(*args, **kwargs)

  def __int__(self, *args, **kwargs) -> int:
    return int(str(self.version).replace('.', ''))

  def __eq__(self, other, *args, **kwargs) -> bool:
    return self.version == other.version, self.name == other.name, self.description == other.description, self.method == other.method

  def __ne__(self, other, *args, **kwargs) -> bool:
    return not self.__eq__(other)