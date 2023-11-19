# coding = utf_8
# NiceDecorator.decorator
"""
module NiceDecorator.decorator.

A decoration module(Decorator)

class:
    Base_Deco(object): Decorator's base class
    group Deco_for_function:
        Deco_Function(Base_Deco): Decorated function Decorator's base class
        Deco_aFunction(Deco_Function): A decorator template class (pass in method)
        Deco_iFunction(Deco_Function): A decorator template class (inheritance)
        Deco_wFunction(Base_Deco): Write Wrapper Return a Decorator
    group Deco_for_class:
        Deco_Class(Base_Deco): Decorated class decorator's object class
        Deco_aClass(Deco_Class): Decorated a Class decorator (pass in method)
        Deco_iClass(Deco_Class): Decorated a Class decorator (inheritance)
    group Deco_combination:
        Deco_Union(Base_Deco): Union the functions
        Deco_List(Base_Deco): List the functions

"""
import functools
from typing import Any, Callable
from . import PASS, set_param, FUNCTION, EMPTY


class Base_Deco(object):
    """
    class NiceDecorator.decorator.Base_Deco(object)

    Decorator's base class

    No use directly!
    """
    def __str__(self):
        return f"Decorator object: {self.__class__}"


# {
class Deco_Function(Base_Deco):
    """
    class NiceDecorator.decorator.Deco_Function(Base_Deco)

    Decorated function decorator's object class

    Please do not use directly!
    """
    
    def __call__(self, func: Callable, /, **c):
        def decofunc(func):
            """
            function decofunc(func)

            A decorator function

            params:
                func: Decorated function

            return:
                wrapper: Decorated function
            """
            nonlocal c
            self._param_it = self._param
            self._param_it.update(c)

            # Action on definition
            _d, wa = set_param.setparam(self._d, self._param_it, "d")
            if "func" in wa:
                func = _d(func=func)
            else:
                _d()

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                _b, wa1 = set_param.setparam(self._b, self._param_it, "b")
                _e, wa2 = set_param.setparam(self._e, self._param_it, "e")

                # Operation before operation
                if "args" in wa1:
                    if "kwargs" in wa1:
                        if "tram" in wa2:
                            args, kwargs, tram = _b(args=args, kwargs=kwargs)
                        else:
                            args, kwargs = _b(args=args, kwargs=kwargs)
                    else:
                        if "tram" in wa2:
                            args, tram = _b(args=args)
                        else:
                            args = _b(args=args)
                else:
                    if "kwargs" in wa1:
                        if "tram" in wa2:
                            kwargs, tram = _b(kwargs=kwargs)
                        else:
                            kwargs = _b(kwargs=kwargs)
                    else:
                        if "tram" in wa2:
                            tram = _b()
                        else:
                            _b()

                res = func(*args, **kwargs)  # Run

                # Operation after operation
                if "tram" in wa2:
                    if "res" in wa2:
                        res = _e(tram=tram, res=res)
                    else:
                        _e(tram=tram)
                else:
                    if "res" in wa2:
                        res = _e(res=res)
                    else:
                        _e()
                return res

            return wrapper
        
        if self.pck:
            return decofunc
        else:
            return decofunc(func)

    @property
    def param(self):
        return self._param

    @property
    def pck(self):
        return self._pck

    @property
    def param_it(self):
        return self._param_it


class Deco_aFunction(Deco_Function):
    """
    class NiceDecorator.decorator.Deco_aFunction(Deco_Function)

    A decorator template class (pass in method)

    method:
        __init__:
            params:
                adef: do some before definition [must be a function] (NiceDecorator.PASS)
                wrap: do some in run [must be a tuple[function, NiceDecorator.FUNCTION, function]] ( (NiceDecorator.PASS, NiceDecorator.FUNCTION, NiceDecorator.PASS) )
                pck: is pack (False)
                --other-- -> **kwargs: set some params(global)

        __call__:
            params:
                --other-- -> **c: set some params(part)

            return:
                function decofunc(func):
                    params:
                        func: Decorated function

                    return:
                        wrapper: Decorated function

                (if not pck, call = decofunc)

    self params:
        wrap: wrapper
        param: global params
        param_it: this params
        pck: is packed

    __str__ -> 'Decorator object: {self.__class__}'
    
    for example:
    >>> decor = decorator.Deco_aFunction(wrap=(timecount.time_start_ns, FUNCTION, timecount.time_end_ns))
    >>> @decor
    >>> def f():
    ...     print(1)
    ...
    >>> a = f()
    >>> b = f()
    >>> print(a, b)
    181000 168600
    
    """

    def __init__(self, adef=PASS, wrap=(PASS, FUNCTION, PASS), pck=False, **kwargs):
        assert wrap[1] == FUNCTION
        self._d = adef
        self._b = wrap[0]
        self._e = wrap[2]
        self._param = kwargs
        self._pck = pck
        self._param_it = self._param


class Deco_iFunction(Deco_Function):
    """
    class NiceDecorator.decorator.Deco_iFunction(Deco_Function)

    A decorator template class (inheritance)

    method:
        __init__:
            params:
                pck: is pack (False)
                --other-- -> **kwargs: set some params(global)

        __call__:
            params:
                --other-- -> **c: set some params(part)

            return:
                function decofunc(func):
                    params:
                        func: Decorated function

                    return:
                        wrapper: Decorated function

                (if not pck, call = decofunc)

        (definition adef,begin,end)

    self params:
        wrap: (self.begin, NiceDecorator.FUNCTION, self.end)
        param: global params
        param_it: this params
        pck: is packed

    __str__ -> Decorator object: {self.__class__}
    
    for example:
    >>> class DECORATOR(decorator.Deco_iFunction):
    ...     def begin(self):
    ...          print("start")
    ...     def end(self):
    ...        print("end")
    ...     def adef(self):
    ...         print("def")
    ...
    >>> @DECORATOR()
    >>> def g():
    ...     print(2)
    ...
    def
    >>> g()
    start
    2
    end
    >>> g()
    start
    2
    end
    
    """

    def __init__(self, pck=False, **kwargs):
        self._d = self.adef
        self._b = self.begin
        self._e = self.end
        self._param = kwargs
        self._param_it = self._param
        self._pck = pck

    def begin(self):
        """
        method begin(self) (in NiceDecorator.decorator.Deco_iFunction)

        pass
        """
        pass

    def end(self):
        """
        method end(self) (in NiceDecorator.decorator.Deco_iFunction)

        pass
        """
        pass

    def adef(self):
        """
        method adef(self) (in NiceDecorator.decorator.Deco_iFunction)

        pass
        """
        pass

    @property
    def wrap(self):
        return (self.adef, self.begin, self.end)


class Deco_wFunction(Base_Deco):
    """
    class Deco_wFunction(Base_Deco)

    Write Wrapper Return a Decorator

    method:
        __init__:
            params:
                func: Decorated function

        __call__:
            params:
                if with paramters:
                    --other-- -> *args, **kwargs: paramters in decorator
                else:
                    f: Decorated function

            return:
                res: Decorated function's response

        __getattr__:
            return:
                self.func.{attribute}

    self params:
        func: decorator
        param_type: is with params ('With' or 'Without')

    __str__ -> 'Decorator object: {self.__class__}'

    for example:
    >>> @decorator.Deco_wFunction
    >>> def decor2(func, *args, **kwargs):
    ...     print("===")
    ...     res = func(*args, **kwargs)
    ...     print("===")
    ...     return res
    ...
    >>> @decor2
    >>> def h():
    ...     print(3)
    ...
    >>> h()
    ===
    3
    ===
    >>> h()
    ===
    3
    ===
    
    """

    def __init__(self, func: Callable):
        arg = set_param.getparam(func)
        param = []
        for _ in arg[1:]:
            if _[0] != "*":
                param.append(_)
        if len(param) > 0:
            @functools.wraps(func)
            def bz(**kw):
                def decorator(f):
                    cc_d = {}
                    for _1, _2 in kw.items():
                        if _1 in param:
                            cc_d[_1] = _2

                    @functools.wraps(f)
                    def wrapper(*listt, **dictt):
                        res = func(f, *listt, **dictt, **cc_d)
                        return res

                    return wrapper

                return decorator

            self._func = bz
            self._type = True
        else:
            @functools.wraps(func)
            def decor(f):
                @functools.wraps(f)
                def wrapper(*listt, **dictt):
                    res = func(f, *listt, **dictt)
                    return res

                return wrapper

            self._func = decor
            self._type = False
        
    def __call__(self, f: Callable, *args: Any, **kwargs):
        if self._type:
            res = self._func(*args, **kwargs)
            return res
        else:
            res = self._func(f)
            return res

    @property
    def func(self):
        return self._func

    @property
    def param_type(self):
        if self._type:
            return "With"
        else:
            return "Without"

    def __getattr__(self, item):
        return getattr(self._func, item)

# }Deco_for_function


# {
class Deco_Class(Base_Deco):
    """
    class NiceDecorator.decorator.Deco_Class(Base_Deco)

    Decorated class decorator's object class

    Please do not use directly!
    """
    def __call__(self, cls=EMPTY, **c):
        def decofunc(cls):
            """
            function decofunc(cls)

            A decorator function

            params:
                cls: Decorated class

            return:
                cls: New class
            """
            self._param_it = self._param
            
            # Append methods
            for f in self.method:
                f_name = f.__name__
                if f_name[0:2] == "__" and f_name[-2:] != "__":
                    f_name = "_" + cls.__name__ + "_" + f_name[3:]  # Change method name during compilation
                setattr(cls, f_name, f)
                
            # Appand attributes
            self._param_it.update(c)
            for p, p_name in self._param_it.items():
                if p_name[0:2] == "__" and p_name[-2:] != "__":
                    p_name = "_" + cls.__name__ + "_" + p_name[3:]  # Change attribute name during compilation
                setattr(cls, p_name, p)
            return cls

        if self._pck:
            return decofunc
        else:
            return decofunc(cls)

    @property
    def pck(self):
        return self._pck

    @property
    def param(self):
        return self._param

    @property
    def param_it(self):
        return self._param_it


class Deco_aClass(Base_Deco):
    """
    class NiceDecorator.decorator.Deco_aClass(NiceDecorator.decorator.Base_Deco)
    
    Decorated a Class decorator (pass in method)

    method:
        __init__:
            params:
                pck: is pack (False)
                method_list: append method list [must be a list] ([])
                --other-- -> **params: append attribute dict(global)
        
        __call__:
            params:
                if self.pck, --other-- -> **c: append attribute dict(this)
                else cls: Decorated class
            
            return:
                function decofunc(cls):
                    params:
                        cls: Decorated class
                    
                    return:
                        cls: New class
                
                (if not self.pck, __call__ = decofunc)
        
    self params:
        method: append method list
        param: append attribute dict(global)
        param_it: append attribute dict(all)
        pck: is packed
    
    __str__ -> 'Decorator object: {self.__class__}'
    """
    def __init__(self, pck=False, method_list=[], **params):
        self._pck = pck
        self._param = params
        self._param_it = self._param
        self.method = method_list


class Deco_iClass(Deco_aClass):
    """
    class NiceDecorator.decorator.Deco_iClass(NiceDecorator.decorator.Deco_aClass)

    Decorated a Class decorator (inheritance)

    method:
        __init__:
            --no params and return--

        __call__:
            params:
                cls: Decorated class

            return:
                cls: New class

        (definition static-add_attr:
            return:
                funcs: append method list [must be a list]
                attrs: append attribute dict [must be a dict]
        )

    self params:
        method: append method list
        param: append attribute dict(global)
        param_it: append attribute dict(all)
        pck: is packed

    __str__ -> 'Decorator object: {self.__class__}'
    """
    def __init__(self):
        self.method, self._param = self.add_attr()
        self._pck = False
        self._param_it = self._param

    @staticmethod
    def add_attr():
        """
        static add_attr() (in NiceDecorator.decorator.Deco_iClass)

        empty

        return:
            funcs: []
            attrs: {}
        """
        attrs = {}
        funcs = []
        return funcs, attrs
# }Deco_for_class


# {
class Deco_Union(Base_Deco):
    """
    class NiceDecorator.decorator.Deco_Union(NiceDecorator.decorator.Base_Deco)

    Union the functions

    method:
        __init__:
            params:
                name: Union name

        __call__:
            params:
                --other-- -> *args, **kwargs: first func parameters

            return:
                if there are not any functions in self.run., None
                else res: last func return

        func:
            params:
                f: add function

            return:
                f: add function
        
        delete:
            params:
                f: remove function

            return:
                f: remove function

    self params:
        run: function list
        name: Union name
        union: union function

    __str__ -> 'Function union object: {self.name}'
    """
    def __init__(self, name=""):
        self.run: list[Callable] = []
        if name == "":
            self.name = self.__class__
        else:
            self.name = name

    def __call__(self, *args, **kwargs):
        return self._union(*args, **kwargs)

    def func(self, f):
        self.run.append(f)
        return f
    
    def delete(self, f):
        while f in self.run:
            self.run.remove(f)
        return f

    def _union(self, *args, **kwargs):
        if len(self.run) == 0:
            return None
        elif len(self.run) == 1:
            return self.run[0](*args, **kwargs)
        else:
            res = self.run[0](*args, **kwargs)
            for f in self.run[1:]:
                if isinstance(res, tuple):
                    if isinstance(res[0], tuple) and isinstance(res[1], dict): # (args, kwargs)
                        # Take the return value of the previous function as a parameter to the following function
                        res = f(*res[0], **res[1])
                    else:  # (args)
                        # Take the return value of the previous function as a parameter to the following function
                        res = f(*res)
                elif isinstance(res, dict):  # (kwargs)
                    # Take the return value of the previous function as a parameter to the following function
                    res = f(**res)
                else:
                    res = f(res)
            return res

    @property
    def union(self):
        """
        method union(self, *args, **kwargs) (in NiceDecorator.decorator.Deco_Union)

        Union function (Take the return value of the previous function as a parameter to the following function)

        params:
            ^self^
            --other-- -> *args, **kwargs: first function parameters

        return:
            res: last function return
        """
        return self._union

    @property
    def __str__(self):
        return f"Function union object: {self.name}"


class Deco_List(Base_Deco):
    """
    class NiceDecorator.decorator.Deco_List(NiceDecorator.decorator.Base_Deco)

    List the functions

    method:
        __init__:
            params:
                name: List name

        __call__:
            params:
                --other-- -> *args, **kwargs: unified parameters

            return:
                res: all func returns

        func:
            params:
                f: add function

            return:
                f: add function
        
        delete:
            params:
                f: remove function

            return:
                f: remove function

    self params:
        run: function list
        name: List name

    __str__ -> 'Function list object: {self.name}'
    """
    def __init__(self, name=""):
        self.run: list[Callable] = []
        if name == "":
            self.name = self.__class__
        else:
            self.name = name

    def __call__(self, *args, **kwargs):
        reses = []
        for c in self.run:
            reses.append(c(*args, **kwargs))

    def func(self, f):
        self.run.append(f)
        return f
    
    def delete(self, f):
        while f in self.run:
            self.run.remove(f)
        return f

    @property
    def __str__(self):
        return f"Function list object: {self.name}"
# }Deco_combination
