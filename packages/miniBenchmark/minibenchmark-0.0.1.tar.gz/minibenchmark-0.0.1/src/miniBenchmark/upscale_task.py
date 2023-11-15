"""
This module provides functionality to iteratively create large memory-consuming tasks (lists of zeros) of increasing size, to determine the limits of memory allocation on a system. It records the time taken for each task and returns a list of these times for successful allocations. It uses the UNIX signal mechanism to introduce a timeout feature for each task, to prevent excessively long runs.

The `upscale_task` function takes a sequence of sizes to attempt to allocate and a timeout duration. It returns a list of times for successful runs and can be verbose based on the `verbose` argument.

Please use this script with caution, as it intentionally pushes the memory limits of the system and could lead to crashes or freezes if not used in a controlled environment.
"""

import gc
import time
import signal
import tracemalloc


# Define the exception to be raised on timeout
class TimeoutException(Exception):
    """Exception used to signal a timeout has occurred."""
    pass

# Signal handler for the alarm
def timeout_handler(signum, frame):
    """Signal handler that raises a TimeoutException when an alarm is received."""
    raise TimeoutException

# Assign the handler for the signal.SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)

def get_task(n):
    """Simulate a memory-consuming task by creating a list of n zeros."""
    return [0] * n

def upscale_task(get_task, factor_sequence, timeout_duration=60*20, verbose=1,
                 repeat=1, custom_clean_up_func = lambda x: None,
                 exterior_seed_seq = None):
    """
    Attempt to create tasks of increasing size based on a given sequence until a timeout or OOM error occurs.

    Parameters:
        factor_sequence (list): A list of integers representing the sizes of tasks to attempt to create.
        timeout_duration (int): The number of seconds before a task times out.
        verbose (int): Verbosity level of the function. If 1, prints messages; if 0, silent mode.

    Returns:
        list: A list of floats representing the times taken for each successful task creation.

    Raises:
        TimeoutException: If a task does not complete within the timeout duration.
        MemoryError: If the system runs out of memory while creating a task.
    """
    times = []  # List to store times of successful runs
    mems = []
    succeeded = []
    if exterior_seed_seq is None:
        exterior_seed_seq = factor_sequence
    for factor in factor_sequence:
        for _ in range(repeat):
                
            try:

                custom_clean_up_func(factor)
                n = factor
                signal.alarm(timeout_duration)  # Set the alarm
                start_time = time.time()
                tracemalloc.start()
                
                if verbose:
                    print(f"Attempting to create task of size: {n}")

                # Perform the task
                task = get_task(n)
                
                elapsed_time = time.time() - start_time
                times.append(elapsed_time)

                if verbose:
                    print(f"Successfully created task with size: {n} in {elapsed_time:.2f} seconds")
                mems.append(tracemalloc.get_traced_memory())
                succeeded.append(factor)
                

            except TimeoutException:
                if verbose:
                    print(f"Task with size: {n} timed out after {timeout_duration} seconds.")
                break
            except MemoryError:
                gc.collect()
                if verbose:
                    print(f"Failed to create a task with size: {n}. Out of Memory error occurred.")
                break
            except Exception as e:
                if verbose:
                    print(f"An unexpected error occurred: {e}")
                break
            # Cleanup
            tracemalloc.stop()
            try:
                del task
            except:
                print("deleting task failed, maybe it is not created")
            gc.collect()
            signal.alarm(0)  # Cancel the alarm
    return times, mems

# Example usage:

#factor_sequence = [1000 * (2 ** i) for i in range(10)]
#timeout_duration = 5  # Timeout after 5 seconds
#times_list = upscale_task(get_task, factor_sequence, timeout_duration)
#print(f"Times of successful runs: {times_list}")

# One can use this to hyperpar tuning for performance or find maximum batch size/ intra parrallel sequence


from .Forests import RF, IF
from .generate_data_tasks import generate_dataset

def example_RF_njobs(njobs):
    ids, X, y   = generate_dataset(n = 2**19, M = 50)
    RF(X, y, n_jobs=njobs, random_state=42)


#seq = [1,2,4,8]
#timeout_duration = 60*100
#times, mems = upscale_task(example_RF_njobs, seq, timeout_duration, repeat = 20)
#print(f"Times of successful runs: {times}, mems {mems}")

