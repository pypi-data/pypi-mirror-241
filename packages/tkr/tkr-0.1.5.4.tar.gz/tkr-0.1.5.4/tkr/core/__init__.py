tkr_version = '0.1.5.4'

def tkr_setup_hook() -> list:
  return (tkr_version, 'tkr', 'toolkitr.tkr', 'tklr.', 'toolkitr.email@gmail.com', 'Python Toolkit')

try:
  with open(f'.pythonlibs/lib/python3.10/site-packages/tkr/core/coreattrs.json', 'w') as file:
  file.write(str({"version": tkr_version}))
except: attrs: str = 'tkr.coreattrs.WriteFailed'