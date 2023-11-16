"""
The tkr.core folder contains core tools for interacting with tkr.

Classes:
- `ChangeLog`: Represents a changelog for a tkr.

Functions:
- `tkr_setup_hook`: Setup hook for tkr.
- `get_changelog`: Gets the changelog for tkr.
- `get_tool_by_name`: Gets a tool by name.
- `get_tool_by_method`: Gets a tool by method.
- `get_tool_by_id`: Gets a tool by id.
- `tkr_help_hook`: Help hook for tkr.
"""

from .changelog import ChangeLog
from .. import resource
from ..abc import (
                             global_tools_by_name, 
                             global_tools_by_method, 
                             global_tools_by_id
)
tkr_version:    str       =  '0.1.7.6'
changelog:      ChangeLog =  ChangeLog()

@resource.notdeprecated
def tkr_setup_hook() -> tuple:
  """
  Setup hook for tkr.
  
  Returns:
  tuple: The setup hook.
  """
  return (tkr_version, 'tkr', 'toolkitr.tkr', 'tklr.', 'toolkitr.email@gmail.com', 'Python Toolkit')

@resource.notdeprecated
def get_changelog(version: str = tkr_version) -> str:
  """
  Get the changelog for the given version.
  
  Parameters:
  version (str): The version to get the changelog for.
  
  Returns:
  str: The changelog for the given version.
  """
  return changelog.cl.get(version, changelog.cl.get(version[:-2], changelog.cl.get(tkr_version, f'No version found. tkr.Versions.{tkr_version}')))

@resource.notdeprecated
def get_tool_by_name(name: str) -> object:
  """
  Get the tool by name.

  Parameters:
  name (str): The name of the tool.
  
  Returns:
  object: The tool.
  """
  return global_tools_by_name.get(name)

@resource.notdeprecated
def get_tool_by_method(method: object) -> list:
  """
  Get the tool by method.

  Parameters:
  method (object): The method of the tool.

  Returns:
  object: The tool.
  """
  return global_tools_by_method.get(method)

@resource.notdeprecated
def get_tool_by_id(id: str) -> list:
  """
  Get the tool by id.

  Parameters:
  id (str): The id of the tool.

  Returns:
  object: The tool.
  """
  return global_tools_by_id.get(id)

@resource.notdeprecated
def tkr_help_hook(print_help: bool = True) -> str:
  """
  Help hook for tkr.

  Parameters:
  print_help (bool): Whether to print help or not.
  
  Returns:
  str: The help hook.
  """
  help_str = f"""
  ## tkr - Python Toolkit
  VERSION: {tkr_version}

  pypi/pip: https://pypi.org/project/tkr/
  github: https://github.com/toolkitr/tkr

  ## Installing/Upgrading

  install > `pip install tkr`
  upgrade > `pip install --upgrade tkr`

  ## Example:
  ```
  import tkr

  def tkr_tool_test() -> list:
    return tkr.ToolProxy

  mytool = tkr.Tool(
    name="mytool",
    version="0.0.1",
    method=tkr_tool_test
  )
  ```
  """
  if print_help == True: print(help_str)
  else: return help_str

try:
  with open(f'.pythonlibs/lib/python3.10/site-packages/tkr/core/coreattrs.json', 'w') as file:
    file.write(str({"version": tkr_version}))
except: attrs: str = 'tkr.coreattrs.WriteFailed'