"""
package NiceDecorator

An easy and nice decorator package

modules:
    decorator: A decoration module(Decorator)
    objective: Package NiceDecorator 's check class module
    separator: Package NiceDecorator 's separator module
    timecount: Package NiceDecorator 's time count module
    set_param: Method of setparam
    model: A decorator model

function:
    PASS(): Pass function
    FUNCTION(): Tag decorated function (CANNOT CALL)

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
            group Deco_combination
                class Deco_Union
                class Deco_List
        model.py
            group function:
                class Deco_Check
                class Deco_Expand
                class Deco_Timer
            group class:
                class Deco_StrOpti
        objective.py
            function STRING
            function INTEGER
            function LIST
        separator.py
            function linesep
            function timesep
            function titlesep
        timecount.py
            group time_count
                function time_start
                function time_end
            group time_count_ns
                function time_start_ns
                function time_end_ns
        set_param.py
            function getparam
            function setparam
    """
)


def PASS():
    """
    function NiceDecorator.PASS()

    Pass function
    """
    pass


def FUNCTION():
    """
    function NiceDecorator.FUNCTION()

    Tag decorated function
    
    CANNOT CALL!
    """
    raise NotImplementedError("CANNOT CALL FUNCTION()!")


class EMPTY(object):
    """
    class NiceDecorator.EMPTY(object)

    Empty class
    """
    pass
