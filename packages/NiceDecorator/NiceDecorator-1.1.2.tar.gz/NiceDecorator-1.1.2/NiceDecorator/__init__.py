"""
package NiceDecorator

An easy and nice decorator package

modules:
    decorator: A decoration module(Decorator)
    objective: Package NiceDecorator 's check class module
    separator: Package NiceDecorator 's separator module
    timecount: Package NiceDecorator 's time count module
    set_param: A param getter and setter module
    model: A decorator model

function:
    PASS(): Pass function
    FUNCTION(): Tag decorated function (CANNOT CALL)

class:
    EMPTY(object): Empty class

help:
    PACKAGE_DIR: Package NiceDecorator 's dir
    CLASSES_MRO: Package NiceDecorator 's inheritance relationship of classes
    FUNCTION_MAGIC_PARAM_HELP: Package NiceDecorator 's magic paramters help
    WARNING: Package NiceDecorator 's used warning
"""


__all__ = ["decorator", "objective", "separator", "timecount", "model",
           "EMPTY",
           "FUNCTION", "PASS",
           "PACKAGE_DIR", "CLASSES_MRO", "FUNCTION_MAGIC_PARAM_HELP", "WARNING"]

PACKAGE_DIR = (
    """
NiceDecorator/
    __init__.py
        class EMPTY
        function PASS
        function FUNCTION
        help PACKAGE_PATH
        help CLASSES_MRO
        help FUNCTION_MAGIC_PARAM_HELP
        help WARNING
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
            class Deco_Timer_ns
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


CLASSES_MRO = (
    """
    decorator.Base_Deco
        decorator.Deco_Function
            decorator.Deco_aFunction
            decorator.Deco_iFunction
                model.Deco_Check
                model.Deco_Expand
                model.Deco_Timer
                model.Deco_Timer_ns
            decorator.Deco_wFunction
        decorator.Deco_Class
            decorator.Deco_aClass
            decorator.Deco_iClass
                decorator.Deco_StrOpti
    """
)


FUNCTION_MAGIC_PARAM_HELP = (
    """
Package NiceDecorator has 5 magic parameters, there are
'func', 'args', 'kwargs', 'res', 'tram'.

The 'func' parameter is used in the function definition section
and is automatically passed in to the decorated function. 
It can be modified. 
If used, MUST RETURN!
In 'model.Deco_Expand', 'func' is extended to the beginning and end of the function, 
but does not need to be returned. 
When used together with other magic parameters, 
it is placed before other magic parameters.

The 'args' parameter is used at the beginning of the function
and is automatically passed in as a positional parameter. 
It can also be modified. 
MUST RETURN!

The 'kwargs' parameter is used at the beginning of the function
and automatically passes in keyword parameters. It can also be modified. 
When passed in simultaneously with 'args' and/or' func '(from model.Deco_Expand), 
it should be placed after both. 
When returned simultaneously with 'args' and/or' tram ', 
placed after' args' and before 'tram'. 
If used, MUST RETURN!

The 'res' paramter is used at the end of the function
and automatically passes in the function return value. 
When used together with 'tram', 
it should be placed before 'tram'. 
If used, MUST RETURN!

The 'tram' parameter is used at the beginning
and end of the function to pass data. 
Returns 'tram' from the beginning of the function, 
located at the end. Received by the end of the function, 
should be at the end, and there is no need to return.
    """
)
WARNING = (
    """
Cannot add '/' to decorative functions
in each decoration function!

The parameters passed in when defining a decorator or decoration
can be received by each decoration function, 
but the positional parameters must be passed
in the format of '_'+passed in function properties ('d','b','e')+'__'+sort+'_'(specifying the passed in function)
or'_'+sort+'_'. 
Keyword parameters can be directly passed in, 
or the passed in function can be specified
in the format of '_'+passed in function properties ('d','b','e')+' __ '+parameter name+' _ '.

In this module, 
the function definition section is specified as'adef' (abbreviated as 'd'), 
the function start section is specified as 'begin' (abbreviated as 'b'), 
and the function end section is specified as 'end' (abbreviated as 'e').

In 'Deco_iClass', add methods and attributes uniformly in add_attr(), 
first return the list of add methods, 
and then return the add attribute dictionary.

In 'Deco_aFunction', 'Deco_iFunction',' Deco_aClass', 'Deco_iClass' and its subclasses, 
if pck is true, parameter passing is allowed, otherwise parameter passing is not allowed.

In 'Deco_aFunction', 'Deco_iFunction' and its subclasses 
are allowed to pass parameter keywords during decoration to indicate adding attributes 
(CANNOT have the same name as 'func' ! Positional parameters CANNOT be passed in!
Should not have the same name as magic parameters!)

In 'Deco_aClass', 'Deco_iClass' and its subclasses, if parameter passing is allowed, 
the positional parameter represents the adding method, 
and the keyword parameter represents the adding property (CANNOT be the same name as 'cls' !)
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
