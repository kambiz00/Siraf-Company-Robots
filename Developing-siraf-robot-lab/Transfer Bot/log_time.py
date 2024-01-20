# import required modules
from datetime import datetime
from termcolor import colored
import os

os.system("")


# decorator to log the start and end time of a function and its duration
def log_the_time(func):
    # define the wrapped function that will execute the original function and log its duration
    def wrapped_func(*args, **kwargs):
        # print a message indicating that the process has started
        print(f'{colored("Robot", "blue")}: process started')

        # record the start time of the function execution
        start_time = datetime.now()

        # execute the original function with its arguments
        func(*args, **kwargs)

        # record the end time of the function execution
        end_time = datetime.now()

        # print a message indicating the end of the process
        print(f'{colored("Robot", "blue")}: end of process')

        # print a message indicating that the duration of the process is being calculated
        print(f'{colored("Robot", "blue")}: calculating the time work')

        # calculate the duration of the function execution
        duration = end_time - start_time
        hours = duration.seconds // 3600
        minutes = duration.seconds // 60
        seconds = duration.seconds % 60

        # print a message indicating the duration of the function execution
        print(
            f"{colored('Robot', 'blue')}: this process took {hours} : {minutes} : {seconds} minute from us{colored('.', 'red')}")

    # return the wrapped function
    return wrapped_func
