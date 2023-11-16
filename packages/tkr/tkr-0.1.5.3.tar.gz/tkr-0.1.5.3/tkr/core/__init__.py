tkr_version = '0.1.5.3'

def tkr_setup_hook() -> list:
  return (tkr_version, 'tkr', 'toolkitr.tkr', 'tklr.', 'toolkitr.email@gmail.com', 'Python Toolkit')

with open(f'toolkitr/tkr/core/coreattrs.json', 'w') as file:
  file.write(str({"version": tkr_version}))