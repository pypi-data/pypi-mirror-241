"""
module NiceDecorator.set_param

A param getter and setter module

function:
    getparam(func): Getter param
    setparam(func, param_it, name): Setter param
"""
import inspect
import time
import re


def getparam(func):
    """
    function NiceDecorator.set_param.getparam(func)

    Getter param

    params:
        func: getter function

    return:
        _args: params
    """
    def have_name(x: inspect.Parameter):
        name = x.name
        if x.kind == inspect.Parameter.VAR_POSITIONAL:
            name = "*" + name
        elif x.kind == inspect.Parameter.VAR_KEYWORD:
            name = "**" + name
        return name

    _args = list(map(have_name, inspect.signature(func).parameters.values()))
    return _args


def setparam(func, param_it, name):
    """
    decorator NiceDecorator.set_param.setparam(func, param_it, name)

    Setter param

    params:
        func: decorated function
        param_it: params
        name: function class

    return:
        func: new function
        will_app: will add params
    """
    _args = getparam(func)
    argc = {}
    posarg_d = {}
    will_app = []

    if "func" in _args and name == "d":
        _args.remove("func")
        will_app.append("func")
    if "args" in _args and name == "b":
        _args.remove("args")
        will_app.append("args")
    if "kwargs" in _args and name == "b":
        _args.remove("kwargs")
        will_app.append("kwargs")
    if "res" in _args and name == "e":
        _args.remove("res")
        will_app.append("res")
    if "tram" in _args and name == "e":
        _args.remove("tram")
        will_app.append("tram")

    for _arg in _args:
        if _arg == "arg":
            for pmk, pmv in param_it.items():
                if re.match("^_[0-9]+_$", pmk):
                    posarg_d[int(pmk[1:-1])] = pmv
                elif re.match(f"^_{name}_[0-9]_$", pmk):
                    posarg_d[int(pmk[3:-1])] = pmv
        else:
            for pmk, pmv in param_it.items():
                if pmk == _arg:
                    argc[pmk] = pmv
                    break
                elif pmk == f"_{name}_{_arg}_":
                    argc[pmk[3:-1]] = pmv
                    break

    def wrapper(**kw):
        assert set(kw.keys()) == set(will_app)
        posargs = list(posarg_d.values())
        res = func(*posargs, **argc, **kw)
        return res

    return wrapper, will_app
