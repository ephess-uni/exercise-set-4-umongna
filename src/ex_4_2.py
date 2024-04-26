""" ex_4_2.py """
from datetime import datetime


def logstamp_to_datetime(datestr):
    """
    To return datatime object by parsing the datastr argument
    """
    dt_obj = datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S')
    return dt_obj


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    test_date = '2022-12-01T01:02:03'
    print(f'{logstamp_to_datetime(test_date)=}')
