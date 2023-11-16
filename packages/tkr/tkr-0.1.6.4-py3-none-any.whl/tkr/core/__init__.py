from .changelog import ChangeLog
tkr_version = '0.1.6.4'
changelog: ChangeLog = ChangeLog()

def tkr_setup_hook() -> list:
  return (tkr_version, 'tkr', 'toolkitr.tkr', 'tklr.', 'toolkitr.email@gmail.com', 'Python Toolkit')

def get_changelog(version: str = tkr_version) -> str:
  return changelog.cl.get(version, changelog.cl.get(version[:-2], changelog.cl.get(tkr_version, f'No version found. tkr.Versions.{tkr_version}')))

try:
  with open(f'.pythonlibs/lib/python3.10/site-packages/tkr/core/coreattrs.json', 'w') as file:
    file.write(str({"version": tkr_version}))
except: attrs: str = 'tkr.coreattrs.WriteFailed'