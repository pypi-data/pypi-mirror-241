from . import core
from . import abc

__version__, __name__, __package__, __author__, __email__, __description__ = core.tkr_setup_hook()

Tool = abc.Tool
ToolProxy = abc.ToolProxy