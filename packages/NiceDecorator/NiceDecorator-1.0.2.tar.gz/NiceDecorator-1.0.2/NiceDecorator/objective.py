"""
module NiceDecorator.objective.

Package NiceDecorator 's check class module

functions:
    Len_Dict(d): Length of dict(number of key value pairs)
    STRING(args, kwargs): A batch force string conversion function
    INTEGER(args, kwargs): A batch force integer conversion function
    LIST(args, kwargs): A batch force list conversion function
"""

from typing import List, Dict


def Len_Dict(d: Dict):
    """
    function NiceDecorator.objective.Len_Dict(d)

    Length of dict(number of key value pairs)

    params:
        d: dict [must be dict]

    return:
        _len_: length of dict
    """
    _len_ = 0
    for _ in d.values():
        if isinstance(_, dict):
            _len_ += Len_Dict(_)
        else:
            _len_ += 1
    return _len_


def STRING(args: List, kwargs: Dict):
    """
    function NiceDecorator.objective.STRING(args, kwargs)

    A batch force string conversion function

    if param is list or tuple, return " ".join(param)
    if param is dict, return " ".join(param.values())
    if param is set, raise
    else return str(param)

    params:
        $args$: the function 's nameless params [must be a list]
        $kwargs$: the function 's with name params [must be a dict]

    return:
        $args$: str nameless params [list]
        $kwargs$: str with name params [dict]
    """
    new_arg = []
    new_kwarg = {}

    def _str_(x):
        if isinstance(x, tuple):
            _1 = x[0]
            _2 = x[1]
            if isinstance(_2, list) or isinstance(_2, tuple):
                new_kwarg[_1] = " ".join(_2)
            elif isinstance(_2, dict):
                new_kwarg[_1] = " ".join(_2.values())
            elif isinstance(_2, set):
                raise TypeError("cannot get 'set' to 'str'")
            else:
                new_kwarg[_1] = str(_2)
        else:
            _ = x
            if isinstance(_, list) or isinstance(_, tuple):
                new_arg.append(" ".join(_))
            elif isinstance(_, dict):
                new_arg.append(" ".join(_.values()))
            elif isinstance(_, set):
                raise TypeError("cannot get 'set' to 'str'")
            else:
                new_arg.append(str(_))

    map(_str_, args, kwargs.items())
    args, kwargs = new_arg, new_kwarg
    return args, kwargs


def INTEGER(args: List, kwargs: Dict):
    """
    function NiceDecorator.objective.INTEGER(args, kwargs)

    A batch force integer conversion function

    if param is list or tuple or set, return length of param
    if param is dict, return number of key value pairs
    if param is str:
        if can int(param), return int(param)
        else return len(param)
    else return int(param)

    params:
        $args$: the function 's nameless params [must be a list]
        $kwargs$: the function 's with name params [must be a dict]

    return:
        $args$: int nameless params [list]
        $kwargs$: int with name params [dict]
    """
    new_arg = []
    new_kwarg = {}

    def _int_(x):
        if isinstance(x, tuple):
            _1 = x[0]
            _2 = x[1]
            if isinstance(_2, list) or isinstance(_2, tuple) or isinstance(_2, set):
                new_kwarg[_1] = len(_2)
            elif isinstance(_2, dict):
                new_kwarg[_1] = Len_Dict(_2)
            elif isinstance(_2, str):
                try:
                    new_kwarg[_1] = int(_2)
                except ValueError:
                    new_kwarg[_1] = len(_2)
            else:
                new_kwarg[_1] = int(_2)
        else:
            _ = x
            if isinstance(_, list) or isinstance(_, tuple) or isinstance(_, set):
                new_arg.append(len(_))
            elif isinstance(_, dict):
                new_arg.append(Len_Dict(_))
            elif isinstance(_, str):
                try:
                    new_arg.append(int(_))
                except ValueError:
                    new_arg.append(len(_))
            else:
                new_arg.append(int(_))

    map(_int_, args, kwargs.items())
    args, kwargs = new_arg, new_kwarg
    return args, kwargs


def LIST(args: List, kwargs: Dict):
    """
    function NiceDecorator.objective.LIST(args, kwargs)

    A batch force list conversion function

    if param is str, return it split(" ")
    if param is int, return list(length = param)
    if param is dict, return it values()
    else return list(param)

    params:
        $args$: the function 's nameless params [must be a list]
        $kwargs$: the function 's with name params [must be a dict]

    return:
        $args$: list nameless params [list]
        $kwargs$: list with name params [dict]
    """
    new_arg = []
    new_kwarg = []

    def _list_(x):
        if isinstance(x, tuple):
            _1 = x[0]
            _2 = x[1]
            if isinstance(_2, str):
                new_kwarg[_1] = _2.split(" ")
            elif isinstance(_2, int):
                new_kwarg[_1] = list(range(_2))
            elif isinstance(_2, dict):
                new_kwarg[_1] = list(_2.values())
            else:
                new_kwarg[_1] = list(_2)
        else:
            _ = x
            if isinstance(_, str):
                new_arg.append(_.split(" "))
            elif isinstance(_, int):
                new_arg.append(list(range(_)))
            elif isinstance(_, dict):
                new_arg.append(list(_.values()))
            else:
                new_arg.append(list(_))

    map(_list_, args, kwargs.items())
    args, kwargs = new_arg, new_kwarg
    return args, kwargs
