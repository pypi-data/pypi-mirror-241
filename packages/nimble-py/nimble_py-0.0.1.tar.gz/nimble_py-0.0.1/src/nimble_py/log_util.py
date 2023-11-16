import logging, logging.handlers
import threading, sys, datetime, traceback

# a thread-local object which can be used anywhere in the app
app_thread_local = threading.local()
def get_thread_local_attribute(attr_name, default_value=None):
    return getattr(app_thread_local, attr_name, default_value)

def set_thread_local_attribute(attr_name, value):
    return setattr(app_thread_local, attr_name, value)   
                         
def set_thread_log_prefix(prefix):
    set_thread_local_attribute('thread_log_prefix', prefix)

                         
from log_util import Logger, FileOnlyLogger
default_logger = Logger(log_file_path=None, console_log_on=True)
# by default, this does not log anything, unless the logger is intialized 
default_file_only_logger = FileOnlyLogger(default_logger) 

def init_file_logger(log_file_path, console_log_on=False, max_bytes=50*1024*1024, backup_count=10,
                    logger=None, log_prefix='', replace_new_lines=None):
    global default_logger
    default_logger = Logger(log_file_path, console_log_on=console_log_on, max_bytes=max_bytes, 
                            backup_count=backup_count, logger=logger, log_prefix=log_prefix, 
                            replace_new_lines=replace_new_lines)

    global default_file_only_logger
    default_file_only_logger = FileOnlyLogger(default_logger)


def log_info(*msgs, **kwargs):
    default_logger.log_info(*msgs, **kwargs)

def log_info_file(*msgs):
    default_logger.log_info_file(*msgs)

def log_error(*msgs):
    default_logger.log_error(*msgs)

def log_error_file(*msgs):
    default_logger.log_error_file(*msgs)

def log_traceback(extra_info_str=''):
    default_logger.log_traceback(extra_info_str)
    
def log_traceback_file(extra_info_str=''):
    default_logger.log_traceback_file(extra_info_str='')


class Logger:

    def __init__(self, log_file_path=None, console_log_on=False, max_bytes=50*1024*1024, backup_count=20, 
        logger=None, log_prefix='', replace_new_lines=None, format1='%(asctime)s %(threadName)s %(filename)s:%(lineno)d: %(message)s'):
        
        self.log_prefix = log_prefix
        self.logger = NoOpLogger()
        self.console_log_on = console_log_on
        self.replace_new_lines = replace_new_lines
        if logger:
            self.logger = logger
            self.log_info(f"Log init with given logger")
        elif log_file_path:
            formatter = logging.Formatter(format1)
            handler = logging.handlers.RotatingFileHandler(log_file_path, maxBytes=max_bytes, backupCount=backup_count)
            handler.setFormatter(formatter)
            logger = logging.getLogger('info')
            logger.setLevel(logging.INFO)
            logger.addHandler(handler)
            self.logger = logger
            self.log_info(f"Log file init at {log_file_path}")

    def log_info(self, *msgs, **kwargs):

        thread_log_prefix = get_thread_local_attribute('thread_log_prefix', '')
        
        log_to_file_only = False
        if 'file_only' in kwargs and kwargs['file_only']:
            log_to_file_only = True
        level_error = False
        if 'level_error' in kwargs and kwargs['level_error']:
            level_error = True

        local_console_logger, local_logger = sys.stdout, self.logger.info
        # if level is error, change console stream and logger level accordingly
        if level_error:
            local_console_logger = sys.stderr
            local_logger = self.logger.error

        log_msg = ' '.join([thread_log_prefix] + [str(msg) for msg in msgs])
        
        if self.replace_new_lines:
            log_msg = log_msg.replace("\n", self.replace_new_lines)

        if local_logger:
            local_logger(log_msg)

        if log_to_file_only:
            return

        if self.console_log_on:
            local_console_logger.write(f'{datetime.datetime.now()} :: {threading.current_thread().name} :: {self.log_prefix}')
            local_console_logger.write(log_msg)
            local_console_logger.write('\n')
            local_console_logger.flush()


    def log_info_file(self, *msgs):
        self.log_info(*msgs, file_only=True)


    def log_error(self, *msgs):
        self.log_info(*msgs, level_error=True)


    def log_error_file(self, *msgs):
        self.log_info(*msgs, level_error=True, file_only=True)

        
    def log_traceback(self, extra_info_str=''):
        error_msg = traceback.format_exc().strip().split('\n')
        self.log_error(f'{extra_info_str}', '::', error_msg[-1], '::\n', '\n'.join(error_msg))
        
    def log_traceback_file(self, extra_info_str=''):
        error_msg = traceback.format_exc().strip().split('\n')
        self.log_error_file(f'{extra_info_str}', '::', error_msg[-1], '::\n', '\n'.join(error_msg))


class NoOpLogger:

    def info(self, msg):
        pass

    error = info


# utility class to use default logger and write all logs to log-file only. No logs go to console.
class FileOnlyLogger:

    def __init__(self, logger):
        
        self.logger = logger
        self.console_log_on = False

        self.log_info = logger.log_info_file
        self.log_error = logger.log_error_file
        self.log_traceback = logger.log_traceback_file

        self.log_info_file = logger.log_info_file
        self.log_error_file = logger.log_error_file
        self.log_traceback_file = logger.log_traceback_file
