import numpy as np
import pandas as pd
import sys
import traceback
import os
import io
import datetime

# useful constants 
ONE_LAKH =    100 * 1000
ONE_MILLION = ONE_LAKH * 10
TEN_LAKHS = ONE_MILLION
FIVE_MILLION = ONE_MILLION * 5
ONE_CRORE =   ONE_MILLION * 10
TEN_CRORE =   ONE_CRORE * 10
ONE_BILLION = TEN_CRORE * 10
HUNDRED_CRORE = ONE_BILLION
ONE_QUADRILLION = ONE_BILLION * ONE_MILLION

# just a helper class to set dynamic properties on any object
class TempClass(object):
    pass

# Helper class to raise for checked exceptions
class ApplicationError(RuntimeError):
    pass

"""
This functions helps in hot reloading a class which has been recently modified.
"""
from importlib import reload
import importlib
def reload_modules(module_list=[]):
    # module_list = ['common_funcs']
    for module in module_list:
        if module in sys.modules:
            reload(sys.modules[module])
            importlib.import_module(module)

def add_function_to_object(object1, function1, class1):
    object1.__dict__[function1.name] = function1.__get__(function1, class1)
            
def format_spoken(num, round_num=False):
    sign = 1
    if num < 0:
        sign = -1
        num = num * -1

    sign_char = ''
    if sign < 1:
        sign_char = '-'

    if num > 999999999:
        if round_num:
            return f'{sign_char}{rund(num / 1000000000)} billion'
        return f'{sign_char}{int(num / 1000000000)}.{int( (num % 1000000000)/1000000 ):02d} billion'
    elif num > 999999:
        if round_num:
            return f'{sign_char}{rund(num / 1000000)} billion'
        return f'{sign_char}{int(num / 1000000)}.{int( (num % 1000000)/1000 ):02d} million'
    else:
        return f'{sign_char}{num}'
    
def format_spoken_indian(num, round_num=False):
    sign = 1
    if num < 0:
        sign = -1
        num = num * -1

    sign_char = ''
    if sign < 1:
        sign_char = '-'

    if num > 9999999:
        if round_num:
            return f'{sign_char}{int( round(num / 10000000) )} crores'
        return f'{sign_char}{int(num / 10000000)}.{int( (num % 10000000)/100000 ):02d} crores'
    elif num > 99999:
        if round_num:
            return f'{sign_char}{int( round(num / 100000) )} lacs'
        return f'{sign_char}{int(num / 100000)}.{int( (num % 100000)/1000 ):02d} lacs'
    elif num > 999:
        if round_num:
            return f'{sign_char}{int( round(num / 1000) )} thousand'
        return f'{sign_char}{int(num / 1000)}.{int( (num % 1000)/10):02d} thousand'
    else:
        return f'{sign_char}{num}'

import random
def generate_pseudo_uuid(n=5, prefix=''):
    now = datetime.datetime.now()
    random_append_str = ''
    for r in range(n):
        random_append_str += str(random.randint(0, 10))
    return prefix + now.strftime("%y%m%d%H%M%S%f") + random_append_str

def is_string(obj):
    try:
        return isinstance(obj, basestring)
    except NameError:
        return isinstance(obj, str)


# -----------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------

# todo: print traceback in proper format
def log_uncaught_exception(exctype, value, tb):
    if issubclass(exctype, KeyboardInterrupt):
        sys.__excepthook__(exctype, value, tb)
        return
    NEWLINE = "\n"
    log_error(f'log_uncaught_exception: exctype: {exctype} - value: {value} - traceback: {NEWLINE.join(traceback.format_tb(tb))}')
    sys.__excepthook__(exctype, value, tb)
sys.excepthook = log_uncaught_exception


# -----------------------------------------------------------------------------------------

def replace_special_characters(input_str):
    return unidecode(unicode(input_str, encoding = "utf-8"))

def template_replace(template_str, map):
    for k, v in map.items():
        template_str = template_str.replace('${%s}' % str(k), str(v))
    return template_str
subst = template_replace


"""
Utility functions for Linux 
"""

import subprocess

def get_num_cpus():
    return int(run_command_return_output("lscpu | grep '^CPU(s):' | awk '{print $2}'").strip())

def get_system_ram():
    return int(run_command_return_output("free -g | grep 'Mem:' | awk '{print $2}'").strip())

# for remote ssh, keys need to be exchanged between systems
def run_command(command, stdin=None, log=True, log_info=log_info, env=None, ip=None, user=None, fail_on_error=True, track_time=False):
    if track_time:
        start = datetime.datetime.now()
    final_command = command
    if ip:
        if "'" in command:
            command = command.replace("'", "'\"'\"'")
            # raise ValueError('Remote command cannot contain single-quote characters. Command given: %s' % command)
        user_str = ''
        if user:
            user_str = '%s@' % user
        final_command = 'ssh %s%s \'%s\'' % (user_str, ip, command)

    if log:
        log_info('Executing command: %s - env: %s' % (final_command, env))
    p = subprocess.Popen(final_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=None, shell=True, env=env)
    for line in iter(p.stdout.readline, b''):
        if log:
            log_info(line.decode('utf-8').strip())
    p.terminate()
    p.wait()
    if p.returncode != 0 and fail_on_error:
        raise ValueError('Process exit status: %s' % p.returncode)
    if log:
        log_info('command return output', p.returncode)

    if track_time:
        end = datetime.datetime.now()
        elapsed = end - start
        return p.returncode, elapsed
    else:
        return p.returncode

cmd = run_command

class IterWrapper(object):
    def __init__(self, iter1):
        self.iter1 = iter1

    def __iter__(self):
        'Returns itself as an iterator object'
        return self

    def __next__(self):
        next1 = self.iter1.__next__()
        if next1:
            return next1.decode('utf-8')
        return None

def run_command_return_iter(command, ip=None, user=None, compress=False, env=None, log=True):
    if compress:
        command += ' | gzip -c '
    final_command = command
    if ip:
        if "'" in command:
            command = command.replace("'", "'\"'\"'")
            # raise ValueError('Remote command cannot contain single-quote characters. Command given: %s' % command)
        user_str = ''
        if user:
            user_str = '%s@' % user
        final_command = 'ssh %s%s \'%s\'' % (user_str, ip, command)
    if log:
        log_info('Executing command: %s' % final_command)
    p = subprocess.Popen(final_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=None, shell=True, env=env)
    if not compress:
        return IterWrapper(iter(p.stdout.readline, b'')), p
    else:
        return IterWrapper(stream_gzip_decompress(iter(p.stdout.readline, b''))), p

# for remote ssh, keys need to be exchanged between systems
def run_command_iter_output(command, ip=None, user=None, log=True, env=None):
    final_command = command
    if ip:
        if "'" in command:
            command = command.replace("'", "'\"'\"'")
            # raise ValueError('Remote command cannot contain single-quote characters. Command given: %s' % command)
        user_str = ''
        if user:
            user_str = '%s@' % user
        final_command = 'ssh %s%s \'%s\'' % (user_str, ip, command)

    if log:
        log_info('Executing command: %s, env: %s' % (final_command, env))
    p = subprocess.Popen(final_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=None, shell=True, env=env)
    for line in iter(p.stdout.readline, b''):
        yield line.decode('utf-8')
    p.terminate()
    p.wait()
    if log:
        log_info('command return output', p.returncode)

def run_command_return_output(command, log=True):
    output_list = []
    for line in run_command_iter_output(command, log=log):
        line = line.strip('\n')
        output_list.append(line)
    return '\n'.join(output_list)

# import pprint, json
# def print_json(json_string):
#     if isinstance(json_string, (dict,list,)):
#         pprint.pprint(json_string)
#     else:
#         pprint.pprint(json.loads(json_string))

# usage:
# timer = Timer()
# ... code to time ...
# timer.get_time()
class Timer:
    def __init__(self):
        self.start = datetime.datetime.now()

    def reset(self):
        self.start = datetime.datetime.now()

    def get_time_hhmmss(self):
        end = datetime.datetime.now()
        time_diff = (end - self.start)
        diff_seconds = time_diff.seconds
        m, s = divmod(diff_seconds, 60)
        h, m = divmod(m, 60)
        ms = (time_diff.microseconds / 1000) % 1000
        time_str = "%02d:%02d:%02d.%03d" % (h, m, s, ms)
        return time_str

    def get_time(self):
        return self.get_time_hhmmss()

    def get_time_and_reset(self):
        time_str = self.get_time_hhmmss()
        self.reset()
        return time_str

import gc
def run_gc():
    # Returns the number of
    # objects it has collected
    # and deallocated
    collected = gc.collect()
 
    # Prints Garbage collector 
    # as 0 object
    log_info("Garbage collector: collected %d objects." % collected)

# ------------------------------------------------

# write to excel
"""
usage:
dfs_map = {'Sheet1':df1, 'sheet2': df2}
file_name = '/tmp/data.xlsx'
write_dfs_to_excel(dfs_map, file_name, percent_cols=[])
"""
def write_dfs_to_excel(dfs_map, file_name, maximize_col_widths=True, percent_cols=[], text_cols=[], index=False):
    log_info(f"Write to excel - {file_name}")
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter', datetime_format='mmm d yyyy hh:mm:ss', date_format='mmm dd yyyy')
    workbook = writer.book
    num_format = workbook.add_format({'num_format': '[>9999999]##\,##\,##\,##0; [>99999]##\,##\,##0; ##,##0'})
    percent_fmt = workbook.add_format({'num_format': '0.00%'})
    text_format = workbook.add_format({'num_format': '@'})
    for sheet, df in dfs_map.items():
        log_info(f"Write to excel - writing sheet - {sheet}")
        df.to_excel(writer,sheet, index=index)

    for sheet, df in dfs_map.items():

        df_sample = df.sample(n=min(df.shape[0], 100)).reset_index(drop=(not index))

        for column in df_sample.columns:
            col_format = None
            max_length_for_col = df_sample[column].astype(str).map(len).max()
            max_length_for_col = max(max_length_for_col, len(column)) # if column name is bigger than column content
            max_length_for_col = min(max_length_for_col, 250) # limit column size to 250 chars
            column_length = max_length_for_col
            if column_length > 150:
                column_length = 150
            col_idx = df_sample.columns.get_loc(column)
            
            if column in text_cols:
                col_format = text_format
            elif 'int' in str(df_sample[column].dtype) or 'float' in str(df_sample[column].dtype):
                if column in percent_cols:
                    col_format = percent_fmt
                else:
                    col_format = num_format
            elif 'datetime64[ns' in str(df_sample[column].dtype):
                column_length = 19
            else:
                # writer.sheets[sheet].set_column(col_idx, col_idx, column_length + 2)
                pass
            
            writer.sheets[sheet].set_column(col_idx, col_idx, column_length + 2, col_format)

    try:
        writer.save()
    except:
        writer.close()

    log_info("Write to excel - done")

# ----------------------------------------------------------

"""
*****  run_in_parallel - Run functions in parallel:

Sample code:

proxies = { "http"  : '', "https" : ''}
fn_specs = []
URLS = [
    'http://some-made-up-domain123.com/',
    'http://www.amazon.com/',
    'http://europe.wsj.com/',
    'http://www.bbc.co.uk/',
    'http://www.google.com/',
]
for url in URLS:
    fn_specs.append((load_url, {'url':url, 'proxies':proxies, 'timeout':10, 'log':False}))
fn_specs.append((cmd, ['echo "1123"']))
results, exception_tuples = run_in_parallel(fn_specs, get_num_cpus(), fork=True, log=False)
ret_vals = [result for fn_spec, result in results]
for exception in exception_tuples:
    exception_to_trace_string(exception[1])

"""
import requests

def run_in_parallel(function_specs, max_workers, fork=True, log=False, logError=False, 
    log_interval=None, executor=None):
    
    if not executor:
        executor_fn = concurrent.futures.ThreadPoolExecutor
        if fork:
            executor_fn = concurrent.futures.ProcessPoolExecutor
        executor = executor_fn(max_workers=max_workers)

        with executor:
            return run_in_parallel_with_given_executor(function_specs, log, logError, log_interval, executor)
    else:
        # do not run with the 'with' clause
        return run_in_parallel_with_given_executor(function_specs, log, logError, log_interval, executor)

def run_in_parallel_with_given_executor(function_specs, log, logError, log_interval, executor):
    results, exceptions = [], []
    future_to_fn = {}
    for fn_spec in function_specs:
        fn, args = fn_spec[0], fn_spec[1]
        if type(args) == list:
            future = executor.submit(fn, *args)
        else:
            future = executor.submit(fn, **args)
        future_to_fn[future] = fn_spec

    log_info_file(f'{len(function_specs)} functions submitted')

    if not log_interval:
        log_interval = len(function_specs) / 10
        log_interval = int(log_interval)
        if log_interval <= 1:
            log_interval = 1
    timer = Timer()
    for future in concurrent.futures.as_completed(future_to_fn):
        fn_spec = future_to_fn[future]
        exception = future.exception()
        if not exception:
            result = future.result()
            results.append( ( fn_spec, result ) )
            if (len(results) % log_interval) == 0:
                pct_done = round(len(results)*100.0 / len(function_specs))
                log_info_file(f'{len(results)} functions done out of {len(function_specs)} ({pct_done}%) - Time taken: {timer.get_time_hhmmss()} - , errors: {len(exceptions)}')
        else:
            # only log first 5 exceptions otherwise it will flood the console/log file
            fn, args = fn_spec[0], fn_spec[1]
            fn_to_string = map_to_string(args)
            exceptions.append( (fn_to_string, exception) )
            if log or logError and len(exceptions) < 5:
                log_error(f'Error for function: {fn} {fn_to_string} - {exception_to_trace_string(exception)}')

    return results, exceptions

def load_url(url, timeout=None, verify=True, getParams=None, post=False, postData=None, headers=None, proxies=None, log=False, logLength=200):
    try:
        if not post:
            res = requests.get(url, verify=verify, proxies=proxies, timeout=timeout, params=getParams, headers=headers)
        else:
            res = requests.post(url, verify=verify, proxies=proxies, timeout=timeout, data=postData, headers=headers)
        if log:
            log_info(f'Url: {url} - result - {res.status_code} - time taken: {res.elapsed.microseconds} - {res.text[:logLength]}')
        return res.text, res.status_code, res.elapsed
    except:
        log_traceback(f'Error for url: {url}')


def exception_to_trace_string(exception):
    if exception.__cause__:
        return '\n'.join(exception.__cause__.args)
    else:
        return '\n'.join(exception.args)


# ----------------------------------------------------------------------

import pickle
def pickle_dump(obj, filepath, remove=[]):
    for key in remove:
        obj.__dict__.pop(key)
    with open(filepath, 'wb') as file:
        pickle.dump(obj, file)
def pickle_load(filepath, put={}):
    with open(filepath, 'rb') as file:
        obj = pickle.load(file)
    for key, attr in put.items():
        obj.__dict__[key] = attr
    return obj

# import codecs
def pickle_dumps_base64(obj):
    return base64.b64encode(pickle.dumps(obj)).decode()
    # return codecs.encode(, "base64").decode()
def pickle_loads_base64(base64_str):
    return pickle.loads(base64.b64decode(base64_str))
 

try:
    display_funcs.html("")
except:
    log_info('importing display_funcs')
    try:
        import display_funcs
        from display_funcs import *
    except Exception as e:
        log_traceback()
        sys.stderr.write(f"Warning: Problem while importing display_funcs - {str(e)}\n")


"""
# sample code

# define the function to be run at regular intervals
def refresh_some_cache():
    log_info('here')

# schedule the task to run every 2 seconds
repeat_timer = RepeatedTimer(interval=2, refresh_some_cache, log_prefix='[Some][Log][Prefix]')

# stop the time if required
repeat_timer.stop()
"""
class RepeatedTimer(object):
    def __init__(self, interval, function, log_prefix = '', log=True, init_interval=None, min_interval=1, max_interval=None, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.min_interval = min_interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.running_since = datetime.datetime(1970, 1, 1)
        self.is_shutdown = False
        self.log_prefix = log_prefix
        self.log = log
        self.max_interval = max_interval
        # make the first call immediately if required
        self.set_timer(interval=init_interval)

    def _run(self):
        set_thread_log_prefix(self.log_prefix)

        if self.should_start_next_run():
            self.set_timer()
            try:
                self.is_running = True
                self.running_since = datetime.datetime.now()
                timer = Timer()
                if self.log:
                    log_info(f"Function Started")
                self.function(*self.args, **self.kwargs)
                if self.log:
                    log_info(f"Function Done - took time {timer.get_time()}")
            except:
                log_traceback(f"Error in calling the Function - took time {timer.get_time()}")
            finally:
                self.is_running = False

    def should_start_next_run(self):
        if not self.is_running:
            return True
        elif self.max_interval:
            delta_seconds = (datetime.datetime.now() - self.running_since).total_seconds()
            if delta_seconds > self.max_interval:
                log_error(f"Previous invocation of the function is running for more than {self.max_interval} seconds - starting a new run")
                return True
            else:
                log_error(f"Previous invocation of the function is still running. delta_seconds: {delta_seconds} . Waiting for {self.min_interval} seconds.")
                self.set_timer(interval=self.min_interval)
                return False
        else:
            log_error(f"Previous invocation of the function is still running. Max interval not set. Waiting for {self.min_interval} seconds.")
            self.set_timer(interval=self.min_interval)
            return False

    def update_interval(self,new_interval):
        
        log_info(f"Updating interval from {self.interval} to {new_interval}")
        self.interval = new_interval

    def set_timer(self, interval=None):

        if not interval:
            interval = self.interval

        if not self.is_shutdown:
            self._timer = threading.Timer(interval, self._run)
            self._timer.daemon=True
            self._timer.start()

    def shutdown(self):
        self.is_shutdown = True
        self._timer.cancel()

"""An atomic, thread-safe incrementing counter."""

class AtomicCounter(object):
        """An atomic, thread-safe counter"""
    
        def __init__(self, initial=0):
            """Initialize a new atomic counter to given initial value"""
            self._value = initial
            self._lock = threading.Lock()
    
        def inc(self, num=1):
            """Atomically increment the counter by num and return the new value"""
            with self._lock:
                self._value += num
                return self._value
    
        def dec(self, num=1):
            """Atomically decrement the counter by num and return the new value"""
            with self._lock:
                self._value -= num
                return self._value
    
        @property
        def value(self):
            return self._value

