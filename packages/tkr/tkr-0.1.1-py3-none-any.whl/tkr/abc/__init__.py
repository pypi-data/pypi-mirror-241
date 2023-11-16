from ._tool import ToolProxy

class Tool(ToolProxy):
  def __init__(self, name: str, version: str, description: str, method: object, *args, **kwargs) -> None:
    self.name = name
    self.version = version
    self.description = description
    self.method = method

  def info(self, *args, **kwargs) -> dict:
    return {
      'name': self.name,
      'version': self.version,
      'description': self.description,
      'method': self.method,
    }

  def __dict__(self, *args, **kwargs) -> dict:
    return self.info()

  def __repr__(self, *args, **kwargs) -> str:
    return f'<Tool name={self.name} version={self.version} description={self.description} method={self.method}>'

  def __str__(self, *args, **kwargs) -> str:
    return self.__repr__()

  def __call__(self, *args, **kwargs) -> object:
    return self.method(*args, **kwargs)