from . import core
from . import abc

__version__, __name__, __package__, __author__, __email__, __description__ = core.tkr_setup_hook()

Tool =              abc.Tool
ToolProxy =         abc.ToolProxy
ToolVersion =       abc.VERSION
changelog =         core.get_changelog
ToolByName =        core.get_tool_by_name
byname =            core.get_tool_by_name
ToolByMethod =      core.get_tool_by_method
bymethod =          core.get_tool_by_method
ToolById =          core.get_tool_by_id
byid =              core.get_tool_by_id
Help =              core.tkr_help_hook
help =              core.tkr_help_hook

__annotations__ = {
    'Tool':         Tool,
    'ToolProxy':    ToolProxy,
    'ToolVersion':  ToolVersion,
    'changelog':    changelog,
    'ToolByName':   ToolByName,
    'ToolByMethod': ToolByMethod,
    'ToolById':     ToolById,
    'help':         help
}