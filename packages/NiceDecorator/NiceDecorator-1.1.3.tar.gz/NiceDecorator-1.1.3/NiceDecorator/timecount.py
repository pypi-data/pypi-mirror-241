"""
module NiceDecorator.timecount

Package NiceDecorator 's time count module

function:
    Group time_count:
        time_start(): Start time count
        time_end(res, tram): End time count and return
    Group time_count_ns:
        time_start_ns(): Start time count
        time_end_ns(res, tram): End time count and return
"""
import time


# {
def time_start():
    """
    function NiceDecorator.timecount.time_start() (Group time_count)

    Start time count

    return:
        $tram$: start time
    """
    tram = time.perf_counter()
    return tram


def time_end(res, tram):
    """
    function NiceDecorator.timecount.time_end() (Group time_count)

    End time count and return

    params:
        $res$: old response
        $tram$: start time

    return:
        $res$: new response
    """
    end = time.perf_counter()
    time_ = end - tram
    if res is None:
        res = time_
    else:
        res = (res, time_)
    return res
# } time_count

# {
def time_start_ns():
    """
    function NiceDecorator.timecount.time_start_ns() (Group time_count_ns)

    Start time count

    return:
        $tram$: start time
    """
    tram = time.perf_counter_ns()
    return tram


def time_end_ns(res, tram):
    """
    function NiceDecorator.timecount.time_end_ns() (Group time_count_ns)

    End time count and return

    params:
        $res$: old response
        $tram$: start time

    return:
        $res$: new response
    """
    end = time.perf_counter_ns()
    time_ = end - tram
    if res is None:
        res = time_
    else:
        res = (res, time_)
    return res
# } time_count_ns
