"""
module NiceDecorator.separator

Package NiceDecorator 's separator module

function:
    linesep(_star, _len): print a line separator
    timesep(_method): print time for separator
"""
import datetime
import time


def linesep(_star: str = "*", _len: int = 8):
    """
    function NiceDecorator.separator.linesep(_star, _len)

    print a line separator

    params:
        _star: separator string [must be a str]
        _len: separator len [must be a int]
    """
    print(_star*_len)


def timesep(_method: str = "DATETIME"):
    """
    function NiceDecorator.separator.timesep(_rou, _method)

    print time for separator

    params:
        _method: time show method [must be str] ("DATETIME")
    """
    if _method == "DATETIME":
        time_ = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")
    elif _method == "CPU":
        time_ = time.time()
    else:
        raise ValueError(_method)

    print(time_)
