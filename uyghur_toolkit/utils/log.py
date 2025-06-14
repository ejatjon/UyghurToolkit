import logging
from enum import IntFlag


class LogLevel(IntFlag):
    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0

LOG_LEVEL=LogLevel.WARNING


class Log:
    def __init__(self,name:str,
                 level:LogLevel=LOG_LEVEL,
                 log_file_name:str=None):
        self.logger=logging.getLogger(name)
        self.console_handler=logging.StreamHandler()
        self.file_handler=None
        self.logger.addHandler(self.console_handler)
        if log_file_name:
            self.file_handler=logging.FileHandler(log_file_name)
            self.logger.addHandler(self.file_handler)
        self.logger.setLevel(level)
        self.setDefaultFormatter()

    def __call__(self, msg,*args, **kwargs):
        self.INFO(msg, *args, **kwargs)

    def set_level(self,level:LogLevel):
        self.logger.setLevel(level)
        self.logger.info("Log level changed to {}".format(level))

    def DEBUG(self, msg, *args, **kwargs):
        self.logger.debug(msg,*args, **kwargs)

    def INFO(self, msg, *args, **kwargs):
        self.logger.info(msg,*args, **kwargs)

    def WARNING(self, msg, *args, **kwargs):
        self.logger.warning(msg,*args, **kwargs)

    def ERROR(self, msg, *args, **kwargs):
        self.logger.error(msg,*args, **kwargs)

    def CRITICAL(self, msg, *args, **kwargs):
        self.logger.critical(msg,*args, **kwargs)

    def EXCEPTION(self, msg, *args, **kwargs):
        self.logger.exception(msg,*args, **kwargs)

    def setLogFile(self,log_file_name:str,**kwargs):
        if self.file_handler:
            self.logger.removeHandler(self.file_handler)
        self.file_handler=logging.FileHandler(log_file_name,**kwargs)
        self.logger.addHandler(self.file_handler)
        self.logger.info("Log file changed to {}".format(log_file_name))

    def removeLogFile(self):
        if self.file_handler:
            self.logger.removeHandler(self.file_handler)
            self.logger.info("Log file removed")
        else:
            self.logger.warning("No log file to remove")

    def setFormatter(self, formatter:logging.Formatter):
        self.console_handler.setFormatter(formatter)
        if self.file_handler:
            self.file_handler.setFormatter(formatter)
        self.logger.info("Log formatter changed")

    def removeFormatter(self):
        self.console_handler.setFormatter(None)
        if self.file_handler:
            self.file_handler.setFormatter(None)
        self.logger.info("Log formatter removed")

    def setDefaultFormatter(self):
        self.removeFormatter()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.setFormatter(formatter)
        self.logger.info("Log formatter set to default")

    def setCustomFormatter(self,formatter:logging.Formatter):
        self.removeFormatter()
        self.setFormatter(formatter)
        self.logger.info("Log formatter set to custom")

    def setLogFileFormater(self,formatter:logging.Formatter):
        if self.file_handler:
            self.file_handler.setFormatter(formatter)
            self.logger.info("Log file formatter changed")
        else:
            self.logger.warning("No log file to change formatter")

    def setDefaultFormatterForConsole(self):
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.console_handler.setFormatter(formatter)
        self.logger.info("Log Console formatter set to default")

    def setDefaultFormatterForLogFile(self):
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.file_handler.setFormatter(formatter)
        self.logger.info("Log file formatter set to default")





