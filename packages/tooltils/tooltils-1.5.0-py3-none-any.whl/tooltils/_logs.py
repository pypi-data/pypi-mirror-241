from logging import getLogger


class levelFilter(object):
    def __init__(self, level):
        self.level = level

    def filter(self, logRecord):
        return logRecord.levelno <= self.level

def create(module: str, level: str, level2: str):
    logger = getLogger(module)

    logger.setLevel(level)
    logger.addFilter(levelFilter(level2))

    return logger

def enable(logger, enabled: bool, closed: bool) -> None:
    if closed: raise ValueError('The logger has already been closed')

    if enabled:
        raise ValueError('The logger is already enabled')
    else:
        logger.disabled = False

def disable(logger, enabled: bool, closed: bool) -> None:
    if closed: raise ValueError('The logger has already been closed')

    if not enabled:
        raise ValueError('The logger is already disabled')
    else:
        logger.disabled = True

def close(logger, closed: bool) -> None:
    if closed:
        raise ValueError('The logger has already been closed')
    else:
        logger.disabled = True
        logger.close()
