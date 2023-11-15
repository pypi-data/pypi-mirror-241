import logging
import colorful as cf
import os
import torch.distributed as dist

__all__ = ["default_logger"]
allocated_loggers = {}

class Logger(logging.Logger):
    DEBUG=logging.DEBUG
    INFO=logging.INFO
    WARN=logging.WARN
    WARNING=logging.WARNING
    FATAL=logging.FATAL
    CRITICAL=logging.CRITICAL
    PRANK = 999
    
    def default_color(self, x): return x
    color_to_rank = [
        cf.italic_red,
        cf.italic_yellow,
        cf.italic_cyan,
        cf.italic_orange,
        cf.italic_blue,
        cf.italic_magenta,
        cf.italic_green,
        cf.italic_purple,
    ]
    def __init__(self, name):
        super(Logger, self).__init__(name)
        self.tag = "Cof"
        self.print_thread = False
        self.print_level = True
        self.rank = 0
        self.name2handler = dict()
        logging.Logger.setLevel(self, logging.DEBUG)

        
    def add_log_file(self, log_file:str, name:str=""):
        if not name: name = log_file
        if name in self.name2handler: return
        handler = logging.FileHandler(log_file)
        self.name2handler[name] = handler
        self.addHandler(handler)
        self.reset_format()

    def set_level_for_handler(self, name:str, level:int):
        if name not in self.name2handler: return
        handler: logging.Handler = self.name2handler[name]
        handler.setLevel(level)
        
    def set_level_for_all(self, level:int):
        for name in self.name2handler:
            handler: logging.Handler = self.name2handler[name]
            handler.setLevel(level)
    
    def setLevel(self, *args, **kwargs):
        print(f"Warn: `setLevel` is not supported, use `set_level_for_all` instead")
        
        
        
    def generate_fmt(self)->logging.StreamHandler:
        level_fmt = "" if not self.print_level else f" [{self.tag} %(levelname)s]"
        basic_fmt = f'[%(asctime)s.%(msecs)03d] {level_fmt}: %(message)s'
        date_fmt = "%Y-%m-%d %H:%M:%S"
        fmt = logging.Formatter(
            fmt = basic_fmt,
            datefmt = date_fmt
        )
        return fmt
        
    def reset_format(self):
        formatter = self.generate_fmt()
        for handler in self.handlers: 
            handler.setFormatter(formatter)
        return self
            
    def _set_tag(self, tag:str):
        self.tag = tag
        self.reset_format()
        return self
    def debug(self, msg:str, color:str='',*args, **kwargs):
        '''print with rank. If color is not specified, use the color format corresponding to the rank'''
        if not dist.is_initialized() or dist.get_rank()==0:
            if not self.isEnabledFor(self.DEBUG): return
            color = getattr(cf, color) if color else self.default_color
            self._log(self.DEBUG, color(msg), args, **kwargs)
    def info(self, msg:str, *args, **kwargs):
        if not dist.is_initialized() or dist.get_rank()==0:
            if self.isEnabledFor(logging.INFO): self._log(logging.INFO, cf.green(msg), args, kwargs)
    def warn(self, msg:str, *args, **kwargs):
        if not dist.is_initialized() or dist.get_rank()==0:
            if self.isEnabledFor(logging.WARN): self._log(logging.WARN, cf.yellow(msg), args, kwargs)
    def error(self, msg:str, *args, **kwargs):
        if not dist.is_initialized() or dist.get_rank()==0:
            if self.isEnabledFor(logging.ERROR): self._log(logging.ERROR, cf.red(msg), args, kwargs)
        
    warning = warn

    
def get_level_from_env(logger_name:str, default_level="info"):
    level = default_level if logger_name not in os.environ else os.environ[logger_name]
    level = level.lower()
    level2num = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warn": logging.WARN,
        "warning": logging.WARN,
        "error": logging.ERROR
    }
    if level in level2num: return level2num[level]
    print(f"Unknown level {level} for logger {logger_name}, use default level {default_level}")
    return level2num[default_level]

    

def get_logger(logger_name="COF_DEBUG",
               enable_console = True)->Logger:
    if logger_name in allocated_loggers: return allocated_loggers[logger_name]
    # why need to call `setLoggerClass` twice? refer to the issue: https://bugs.python.org/issue37258
    logging.setLoggerClass(Logger)
    logger:Logger = logging.getLogger(logger_name)
    logging.setLoggerClass(logging.Logger)
    # Initilize level from environment. If not specified, use INFO
    if enable_console:
        streamHandler = logging.StreamHandler()
        name = logger_name
        logger.name2handler[name] = streamHandler
        streamHandler.setLevel(get_level_from_env(logger_name))
        logger.addHandler(streamHandler)
    logger.reset_format()
    allocated_loggers[logger_name] = logger
    return logger

default_logger = get_logger()
