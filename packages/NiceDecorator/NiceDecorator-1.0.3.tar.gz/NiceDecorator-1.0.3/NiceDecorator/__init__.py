"""
package deco

An easy and nice decorator package

modules:
    deco: A decoration module(Decorator)
    objective: Package deco 's check class module
    separator: Package deco 's separator module
    timecount: Package deco 's time count module
    set_param: Fast of setparam
    model: A decorator model

function:
    PASS(): Pass function
    FUNCTION(): Characteristic function

class:
    EMPTY(object): Empty class

local:
    get_path: package's path
"""


__all__ = ["decorator", "objective", "separator", "timecount", "model",
           "EMPTY",
           "FUNCTION", "PASS",
           "get_path"]

get_path = (
    """
    NiceDecorator/
        __init__.py
            class EMPTY
            function PASS
            function FUNCTION
            local get_path
        decorator.py
            class Base_Deco
            group Deco_for_function:
                class Deco_Function
                class Deco_aFunction
                class Deco_iFunction
                class Deco_wFunction
            group Deco_for_class:
                class Deco_Class
                class Deco_aClass
                class Deco_iClass
            group Deco_Union
                class Deco_Union
        model.py
            group function:
                class Deco_Check
                class Deco_Expand
                class Deco_Timer
            group class:
                class Deco_StrOpti
        objective.py
            function Len_Dict
            function STRING
            function INTEGER
            function LIST
        separator.py
            function linesep
            function timesep
        set_param.py
            function getparam
            function setparam
        timecount.py
            group time_count
                function time_start
                function time_end
            group time_count_ns
                function time_start_ns
                function time_end_ns
    """
)


def PASS():
    """
    function deco.PASS()

    Pass function
    """
    pass


def FUNCTION():
    """
    function deco.FUNCTION()

    Characteristic function
    """
    raise NotImplementedError


class EMPTY(object):
    """
    class deco.EMPTY(object)

    Empty class
    """
    pass
