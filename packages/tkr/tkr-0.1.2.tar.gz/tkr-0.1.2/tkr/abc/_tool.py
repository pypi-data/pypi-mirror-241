from typing import (Optional, TypeVar, Protocol, runtime_checkable)

@runtime_checkable
class ToolProxy(Protocol):
  name: str
  version: str
  description: str
  method: object