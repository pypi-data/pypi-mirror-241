from typing import Callable, TextIO
from datetime import datetime
from functools import wraps
import tracemalloc as tm
import os, csv


def get_current_time() -> str:
    '''Returns the current time in the 'HH:MM:SS.SSS' format as a string.'''
    t = datetime.now()
    return str(t.hour).zfill(2)+':'+str(t.minute).zfill(2)+':'+str(t.second).zfill(2)+'.'+str(t.microsecond)[:3].zfill(3)

def profiler(path:TextIO):
    '''
    A decorator for profiling the execution time and memory usage of a function and logging the results to a CSV file.

    Args:
    -----
        - `path` (TextIO): A file object (opened in 'a' mode) to write the profiling results in CSV format.

    Usage:
    ------
    >>> @profiler('path/to/file.csv')
    >>> def example_function(arg1, arg2):
    ...    # function implementation

    The decorator logs the following information to the CSV file:
        - `function` (str): The name of the decorated function.
        - `time_start` (str): The start time of the function execution in 'HH:MM:SS.SSS' format.
        - `time_end` (str): The end time of the function execution in 'HH:MM:SS.SSS' format.
        - `memory_MiB` (float): The memory usage of the function in MB (megabytes).
        - `process_id` (int): The process ID (PID) of the Python process running the function.

    Example CSV structure:
    ----------------------
        function | time_start   | time_end     | memory_MB | process_id
        ---------------------------------------------------------------
        func1    | 10:30:45.123 | 10:31:12.45  | 15.234    | 12345
        func2    | 10:32:18.78  | 10:32:25.678 | 12.345    | 67890
    '''
    def decorator(func:Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = get_current_time()
            tm.start()
            result = func(*args, **kwargs)
            memory = round(tm.get_traced_memory()[1] / 1024**2, 4)
            tm.stop()
            end = get_current_time()
            pid = os.getpid()

            with open(path, 'a', newline='') as file:
                writer = csv.writer(file, delimiter='|')

                if os.path.getsize(path)==0:
                    writer.writerow(['function', 'time_start', 'time_end', 'memory_MB', 'process_id'])

                writer.writerow([func.__name__, start, end, memory, pid])

            return result
        return wrapper
    return decorator