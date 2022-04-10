import logging
from enum import Enum


class Logger():
    '''
    Define and return a new logger
    '''
    def __init__(self, module):
        self.module = module
        self.logger = logging.getLogger(f'{module}')
        self.logger.setLevel(logging.DEBUG)
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(name)s - %(levelname)s: %(message)s')
        consoleHandler.setFormatter(formatter)
        self.logger.addHandler(consoleHandler)

    def __repr__(self):
        return repr(f"Logger {self.logger} for {self.module} module")

    def message(self, level, message):
        if level == Level.DEBUG:
            self.logger.debug(message)
        elif level == Level.INFO:
            self.logger.info(message)
        elif level == Level.WARNING:
            self.logger.warning(message)
        elif level == Level.ERROR:
            self.logger.error(message)
        elif level == Level.CRITICAL:
            self.logger.critical(message)


class Level(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL
