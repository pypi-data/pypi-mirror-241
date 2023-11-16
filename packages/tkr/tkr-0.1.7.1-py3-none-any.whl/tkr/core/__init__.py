from .changelog import ChangeLog
from ..abc import (
                        global_tools_by_name, 
                        global_tools_by_method, 
                        global_tools_by_id
)
tkr_version =           '0.1.7.1'
changelog: ChangeLog =  ChangeLog()

def tkr_setup_hook() -> list:
  return (tkr_version, 'tkr', 'toolkitr.tkr', 'tklr.', 'toolkitr.email@gmail.com', 'Python Toolkit')

def get_changelog(version: str = tkr_version) -> str:
  return changelog.cl.get(version, changelog.cl.get(version[:-2], changelog.cl.get(tkr_version, f'No version found. tkr.Versions.{tkr_version}')))

def get_tool_by_name(name: str) -> object:
  return global_tools_by_name.get(name)

def get_tool_by_method(method: object) -> list:
  return global_tools_by_method.get(method)

def get_tool_by_id(id: str) -> list:
  return global_tools_by_id.get(id)

def tkr_help_hook(print_help: bool = True) -> str:
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