from typing import (Optional, TypeVar, Protocol, runtime_checkable)

abc_types: tuple = (
  'TOOL.TKR.PROXY',
  'TOOL.TKR.CLASSIC'
)

VERSION: str = abc_types[0]

@runtime_checkable
class ToolProxy(Protocol):
  name: str
  __name__: str
  version: str
  __version__: str
  description: str
  __description__: str
  method: object
  __method__: object
  type: str = VERSION
  __type__: str = VERSION