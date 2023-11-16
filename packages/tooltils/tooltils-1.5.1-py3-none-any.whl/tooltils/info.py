"""General installation information"""


class _bm:
    from logging import basicConfig, DEBUG, INFO, WARN, ERROR, CRITICAL
    from os.path import exists, abspath
    from json import load, dumps
    from typing import Union
    from os import listdir

    from ._logs import create, enable, disable, close

    class LoggingLevel:
        pass

    defaultData: dict = {
        "cache": {
            "errors": {},
            "global": {
                # "configMethodValues": {}
            },
            "info": {},
            "main": {},
            "requests": {
                "verifiableTimesChecked": 0,
                "verifiableNetworkList": {},
                "connectedTimesChecked": 0,
                "connectedNetworkList": {}
            },
            "sys.info": {},
            "sys": {}
        },
        "config": {
            "errors": {},
            "global": {
                # "config": {
                #     "runConfigMethodAlways": False,
                #     "checkMethodForSafety": True
                # } 
            },
            "info": {},
            "main": {},
            "requests": {
                # "defaultVerificationMethod": True,
                "verifiableCachingCheck": 50,
                "connectedCachingCheck": 50,
                "verifiableCaching": False,
                "connectedCaching": False
            },
            "sys.info": {},
            "sys": {}
        }
    }

    # actualConfig: dict = defaultConfig
    openData = None


location: str = str('/'.join(__file__.split('/')[:-2]) + '/')
"""The path of the current installation of tooltils"""

if not _bm.exists(location + 'data.json'):
    with open(location + 'data.json', 'a+') as _f:
        _f.write(_bm.dumps(_bm.defaultData, indent=4))

with open(location + 'LICENSE') as _f:
    _lt: str = _f.read()
    
with open(location + 'README.md') as _f:
    _ld: str = _f.read()

def _getData():
    if _bm.openData is None:
        _bm.openData = open(location + 'data.json', 'r+')

    return _bm.openData

def _loadCache(module: str='') -> dict:
    _f = _getData()
    data: dict = _bm.load(_f)['cache']
    _f.seek(0)

    if module == '':
        return data
    else:
        return data[module]

def _editCache(module: str, option: dict, subclass: str='') -> None:
    _f = _getData()
    data = _bm.load(_f)

    if subclass:
        data['cache'][module][subclass].update(option)
    else:
        data['cache'][module].update(option)

    _f.seek(0)
    _f.truncate()
    _f.write(_bm.dumps(data, indent=4))
    _f.seek(0)

def _deleteCacheKey(module: str, key: str, subclass: str='') -> None:
    _f = _getData()
    data = _bm.load(_f)

    if subclass:
        keys = data['cache'][module][subclass].keys()
    else:
        keys = data['cache'][module].keys()

    for i in list(keys):
        if key == i:
            if subclass:
                data['cache'][module][subclass].pop(i)
            else:
                data['cache'][module].pop(i)

    _f.seek(0)
    _f.truncate()
    _f.write(_bm.dumps(data, indent=4))
    _f.seek(0)

def _loadConfig(module: str='') -> dict:
    _f = _getData()
    data: dict = _bm.load(_f)['config']
    _f.seek(0)

    if module == '':
        return data
    else:
        return data[module]

def _editConfig(module: str, option: dict, subclass: str='') -> None:
    _f = _getData()
    data: dict = _bm.load(_f)

    if subclass:
        data['config'][module][subclass].update(option)
    else:
        data['config'][module].update(option)

    _f.seek(0)
    _f.truncate()
    _f.write(_bm.dumps(data, indent=4))
    _f.seek(0)

def clearCache(module: str=None) -> None:
    """Clear the file cache of tooltils or a specific module within"""

    module: str = str(module).lower()
    _f          = _getData()
    wdata: dict = _bm.load(_f)

    if module == 'none':
        data: dict = _bm.defaultData['cache']
    else:
        data: dict = wdata['cache']

        try:
            data.update(_bm.defaultData['cache'][module])
        except KeyError:
            raise FileNotFoundError('Cache module not found')
        
    wdata['cache'] = data

    _f.seek(0)
    _f.truncate(0)
    _f.write(_bm.dumps(wdata, indent=4))
    _f.seek(0)

def clearConfig(module: str=None) -> None:
    """Revert the config of tooltils or a specific module within"""

    module: str = str(module).lower()
    _f          = _getData()
    wdata: dict = _bm.load(_f)

    if module == 'none':
        data: dict = _bm.defaultData['config']
    else:
        data: dict = wdata['config']

        try:
            data.update(_bm.defaultData['config'][module])
        except KeyError:
            raise FileNotFoundError('Config module not found')
        
    wdata['config'] = data

    _f.seek(0)
    _f.truncate(0)
    _f.write(_bm.dumps(wdata, indent=4))
    _f.seek(0)

def clearData() -> None:
    """Clear the cache and config of tooltils"""

    clearCache()
    clearConfig()

class logger():
    """Create a logging instance for tooltils modules only"""

    def enable(self) -> None:
        _bm.enable(self._logger, self.enabled, self.closed)

    def disable(self) -> None:
        _bm.disable(self._logger, self.enabled, self.closed)
    
    def close(self) -> None:
        _bm.close(self._logger, self.closed)

    @property
    def module(self) -> str:
        """What module the logging is enabled for"""

        return self._module
    
    @module.setter
    def module(self, value):
        raise AttributeError('Module property cannot be changed')

    @property
    def level(self) -> _bm.Union[str, int, _bm.LoggingLevel]:
        """What level of logging is being used"""

        return self._level
    
    @level.setter
    def level(self, value):
        raise AttributeError('Level property cannot be changed')
    
    @property
    def level2(self) -> _bm.Union[str, int, _bm.LoggingLevel]:
        """What max level of logging is being used"""

        return self._level2
    
    @level2.setter
    def level2(self, value):
        raise AttributeError('Level2 property cannot be changed')

    @property
    def enabled(self) -> bool:
        """Whether the logger is enabled"""

        return self._enabled
    
    @enabled.setter
    def enabled(self, value):
        raise AttributeError('Enabled property cannot be changed')

    @property
    def closed(self) -> bool:
        """Whether the logger has been closed"""

        return self._closed
    
    @closed.setter
    def closed(self, value):
        raise AttributeError('Closed property cannot be changed')
    
    def enable(self) -> None:
        """Enable the logger instance"""

        self._enabled = not _bm.enable(self._logger, self.enabled, self.closed)
    
    def disable(self) -> None:
        """Disable the logger instance"""

        self._enabled = bool(_bm.disable(self._logger, self.enabled, self.closed))
    
    def close(self) -> None:
        """Close the logger instance"""
        
        self._disabled = True
        self._closed   = not _bm.close(self._logger, self.closed)

    def __init__(self, 
                 module: str='ALL', 
                 level: _bm.Union[str, int, _bm.LoggingLevel]='ALL',
                 level2: _bm.Union[str, int, _bm.LoggingLevel]='ALL'
                 ) -> None:
        if type(module) is str: module = module.upper()
        if type(level) is str: level = level.upper()
        if type(level2) is str: level2 = level2.upper()
        
        if type(module) is not str:
            raise TypeError('Module must be a valid \'str\' instance')
        elif module not in ('', 'ALL', 'MAIN', 'REQUESTS', 'SYS'):
            raise ValueError('Unknown module \'{}\''.format(module))
        else:
            self._module: str = module

            if module == '' or module == 'ALL' or module == 'MAIN':
                self._module: str = 'tooltils'
            else:
                self._module: str = 'tooltils.' + module.lower()
        for i in (('level', level), ('level2', level2)):
            if not isinstance(i[1], (str, int, _bm.DEBUG, _bm.INFO, _bm.WARN,
                                     _bm.ERROR, _bm.CRITICAL)):
                raise TypeError(f'{i[0]} must be a valid \'str\', \'int\' or \'logging\' level instance')
            elif i[1] not in ('ALL', 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL', 10, 20, 30, 40, 50):
                raise ValueError('Invalid level \'{}\''.format(i[1]))
            else:
                if i[0] == 'level':
                    if level == 'ALL':
                        self._level = _bm.DEBUG
                    else:
                        self._level = level
                else:
                    if level2 == 'ALL':
                        self._level2 = _bm.CRITICAL
                    else:
                        self._level2 = level2

        self._logger  = _bm.create(self._module, self._level, self._level2)
        self._closed  = False
        self._enabled = True

        _bm.basicConfig(format=
                        '[%(asctime)s] [{}/%(levelname)s]: %(message)s'.format(self._module),
                        datefmt='%I:%M:%S')

    def __str__(self) -> str:
        module: str = 'ALL' if not self.module else self.module.upper()
        state:  str = 'on' if self.enabled else 'off'

        return f'<Logger instance: [{state}] -> [{module}]>'

author:      str = str('feetbots')
"""The creator of tooltils (is and always will be feetbots)"""
version:     str = str('1.5.1')
"""The current installation version"""
released:    str = str('16/11/2023')
"""Release date of the current version"""
license:     str = str(_lt)
"""The content of the currently used license"""
description: str = str('A lightweight python utility package built on the standard library')
"""The short description of tooltils"""
long_description: str = str(_ld)
"""The long description of tooltils (README.md)"""

def _getFiles(dir: str) -> list:
    fileList: list = []

    for i in _bm.listdir(location + dir):
        fileList.append(location + dir + '/' + i)
        
    return fileList

lines: int = int(0)
"""How many lines of code in this version"""
_files: list = _getFiles('') + _getFiles('tooltils/requests') + \
               _getFiles('tooltils/sys')

for i in _files:
    if i.endswith(('LICENSE', '.DS_Store', '__pycache__', '.git')):
        _files.remove(i)

# remove these seperately because they would not be removed from the endswith
# statement for whatever reason
_files.remove(location + '/API.md')
_files.remove(location + '/CHANGELOG.md')

for i in _files:
    try:
        with open(i) as _f:
            lines += len(_f.readlines())
    except (IsADirectoryError, UnicodeDecodeError):
        pass

del _getFiles, _files, _lt, _ld
