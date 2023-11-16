class ChangeLog:
  def __init__(self):
    self.cl = {'0.1.6': self.v016}
  @property
  def v016(self) -> str:
    return """
    # Changelog

All notable changes to tkr will be documented in this file

## [V0.1.6]

### Added

- tkr.core coreattrs.json: Working on implementing a system of change during runtime
- tkr.core.get_changelog: tkr.changelog(version = '0.1.6.3') # Defaults to current version.

### Changed

- tkr.Tool attribute & variable updates: More functions, attributes, and variables in tkr.abc.Tool and tkr.abc._tool.ToolProxy 

### Deprecated

- No deprecated features: N/A

### Fixed

- toolkitr.tkr install error: Fixed all errors when installing using pip/pypi

### Removed

- tkr.set_abc: Removed tkr.abc.set_abc and tkr.core.set_abc

### Security

- tkr.core.coreattrs: Added simple try/except handling for any possible errors. On error creates variable attrs at tkr.core.attrs"""