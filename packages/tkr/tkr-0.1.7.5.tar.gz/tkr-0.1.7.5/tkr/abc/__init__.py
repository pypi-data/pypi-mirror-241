import asyncio
import inspect
from ._tool import ToolProxy

abc_types: tuple = (
                                'TOOL.TKR.PROXY',
                                'TOOL.TKR.CLASSIC'
)

VERSION: str =                  abc_types[1]

global_tools_by_name:   dict =  {} 
global_tools_by_method: dict =  {}
global_tools_by_id: dict =      {}

abc_id: id =                    id

class Tool(ToolProxy):
  slots: tuple =                  ('name', 'version', 'description', 'method', '__name__', '__version__', '__description__', '__method__', 'type', '__type__', 'id', '__id__')

  def __init__(self, method: object, name: str='Tool.DefaultName', version: str='Tool.NoVersion', description: str='Tool.Description', id: str=None, *args, **kwargs) -> None:
    if global_tools_by_name.get(name) is not None:
      tool_new_name: str = f'Tool.InUseNameDefault.{hex(abc_id(self))}'
      print(Exception(f'Tool.name=<"{name}"> is already in use. Using {tool_new_name}'))
      name: str =                tool_new_name

    global_tools_by_name[name] = self

    if id is None:
      id: str = f'Tool.Id.{hex(abc_id(self))}'
    global_tools_by_id[id] = self


    self.id: str =               id
    self.__id__: str =           self.id
    self.name: str =             name
    self.__name__: str =         self.name
    self.version: str =          version
    self.__version__: str =      self.version
    self.description: str =      description
    self.__description__: str =  self.description
    self.desc: str =             self.description
    self.__desc__: str =         self.description
    self.method: str =           method
    self.__method__: str =       self.method
    self.func: str =             self.method
    self.__func__: str =         self.method
    self.type: str =             VERSION
    self.__type__: str =         self.type

    if global_tools_by_method.get(self.method) is not None:
      if isinstance(global_tools_by_method[self.method], list):
        global_tools_by_method[self.method].append(self)
    else:
      global_tools_by_method[self.method] = [self]

  def register(self, method: object = None, name: str='Tool.DefaultName', version: str='Tool.NoVersion', description: str='Tool.Description', type: str = abc_types[1], id: str=None, *args, **kwargs) -> ToolProxy:
    if method is None: method = self.method
    self.__init__(method, name, version, description, id, *args, **kwargs)
    return self

  def update(self, method: object = None, name: str='Tool.DefaultName', version: str='Tool.NoVersion', description: str='Tool.Description', type: str = abc_types[1], id: str=None, *args, **kwargs) -> ToolProxy:
    self.register(method=method, name=name, version=version, description=description, type=type, id=id, *args, **kwargs)
    return self

  def run(self, *args, **kwargs):
    if inspect.iscoroutinefunction(self.method): out: object = asyncio.run(self.method(*args, **kwargs))
    else: out: object = self.method(*args, **kwargs)
    return out

  def info(self, *args, **kwargs) -> dict:
    return {
      'name': self.name,
      'version': self.version,
      'id': self.id,
      'description': self.description,
      'method': self.method,
      'type': self.type
    }

  def __dict__(self, *args, **kwargs) -> dict:
    return self.info()

  def __tuple__(self, *args, **kwargs) -> tuple:
    return (self.name, self.version, self.id, self.description, self.method, self.type)

  def __list__(self, *args, **kwargs) -> list:
    return [self.name, self.version, self.id, self.description, self.method, self.type]

  def __repr__(self, *args, **kwargs) -> str:
    return f'<Tool name={self.name} version={self.version} id={self.id} description={self.description} method={self.method} type={self.type}>'

  def __str__(self, *args, **kwargs) -> str:
    return self.__repr__()

  def __call__(self, *args, **kwargs) -> object:
    return self.method(*args, **kwargs)

  def __int__(self, *args, **kwargs) -> int:
    return int(str(self.version).replace('.', ''))

  def __eq__(self, other, *args, **kwargs) -> bool:
    return self.name == other.name, self.version == other.version, self.id == other.id, self.description == other.description, self.method == other.method, self.type == other.type

  def __ne__(self, other, *args, **kwargs) -> bool:
    return self.name != other.name, self.version != other.version, self.id != other.id, self.description != other.description, self.method != other.method, self.type != other.type

  def help(self, print_help: bool=True, *args, **kwargs) -> str:
    help_str: str = """
    tkr.abc.Tool
    
    method: lambda methods, functions, classes, etc
    
    tlkr.abc.Tool.register(method<Optional>, name<Optional>, version<Optional>, description<Optional>, type<Optional>, id<Optional>)
    
    tlkr.abc.Tool.update = .register() # Same as tlkr.abc.Tool.register()
    
    print(tlkr.abc.Tool.__annotations__)
    
    tlkr.abc.Tool.run(*args, **kwargs) # Runs current method
    
    ### CURRENT METHOD CAN ALSO BE CAN WITH __CALL__###
    EXAMPLE: mytool = Tool(method=my_function)
    
    mytool() <- RUNS my_function
    """
    if print_help == True: print(help_str)
    else: return help_str