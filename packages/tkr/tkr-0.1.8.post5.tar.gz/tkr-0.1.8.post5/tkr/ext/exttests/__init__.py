import requests
from ... import resource

@resource.notdeprecated
class Driver:
  def __init__(self, path: str='README.md', *args, **kwargs) -> None:
    self.__baseurl: str = 'https://raw.githubusercontent.com/toolkitr/tkr/main/test/'
    self.__file: str = f'{self.__baseurl}{path}'
    self.__content: object = self.__get_content()

  @resource.notdeprecated
  def __repr__(self) -> str:
    return self.__content

  @resource.notdeprecated
  def __str__(self) -> str:
    return self.__content

  @resource.notdeprecated
  def __get_content(self) -> str:
    try:
      return requests.get(self.__file).text
    except: 
      try: requests.get(self.__file)
      except: return 'tkr.ext.Driver.FilePathError'
    
  @resource.notdeprecated
  def __call__(self, path: str=None, *args, **kwargs) -> str:
    if path is None: return self.__content
    else:
      self.__file: str = f'{self.__baseurl}{path}'
      self.__content: object = self.__get_content()
      return self.__content