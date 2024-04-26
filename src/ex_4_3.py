""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    To return the time difference between the shutdowns.
    """
    shutdownlist = get_shutdown_events(logfile)
    initial_shutdown = logstamp_to_datetime(shutdownlist[0].split(" ")[1])
    last_shutdown = logstamp_to_datetime(shutdownlist[-1].split(" ")[1])
    time_diff = (last_shutdown - initial_shutdown)
    return time_diff


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
