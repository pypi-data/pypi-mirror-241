from .changelog import changelog
tkr_version = '0.1.6.2'

def tkr_setup_hook() -> list:
  return (tkr_version, 'tkr', 'toolkitr.tkr', 'tklr.', 'toolkitr.email@gmail.com', 'Python Toolkit')

def get_changelog(version: str = tkr_version) -> str:
  return changelog.get(version, 'Changelog not found. Try a format like this: (example: 0.0.0.0) -> version=\'0.0.0.0\'')

try:
  with open(f'.pythonlibs/lib/python3.10/site-packages/tkr/core/coreattrs.json', 'w') as file:
    file.write(str({"version": tkr_version}))
except: attrs: str = 'tkr.coreattrs.WriteFailed'