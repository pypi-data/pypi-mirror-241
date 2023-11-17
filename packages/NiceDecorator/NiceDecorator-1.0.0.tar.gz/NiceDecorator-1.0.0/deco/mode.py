"""
module decor.mode.

A decorator mode

class:
    group function:
        Deco_Check(decor.decor.Deco_iFunction): A decorator Check class
        Deco_Expand(decor.decor.Deco_iFunction): Deco_Function 's Expand class
        Deco_Timer(decor.decor.Deco_iFunction): Deco_Function 's Timer Count Class
    group class:
        Deco_StrOpti(decor.decor.Deco_iClass): A print Optimizer

"""
from sys import getsizeof
from typing import Iterable

from . import decorator, set_param, timecount


# {
class Deco_Check(decorator.Deco_iFunction):
    """
    class Deco_Check(decor.decor.decor.Deco_iFunction)

    A decorator Check class

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

        (definition if_, true_, false_, begin, end)

    self params:
        wrap: (self.begin, decor.FUNCTION, self.end)
        param: global params
        param_it: this params
        pck: is packed

    __str__ -> 'Decorator object: {self.__class__}'
    """
    def if_(self, str_con="True"):
        """
        method if_(self) (in decor.mode.Deco_Check)

        Return str_con bool

        params:
            str_con: condition

        return:
            bool_con: bool
        """
        return bool(eval(str_con))

    def true_(self):
        """
        method true_(self) (in decor.mode.Deco_Check)

        run at True
        pass
        """
        pass

    def false_(self):
        """
        method false_(self) (in decor.mode.Deco_Check)

        run at False
        pass
        """
        pass

    @property
    def adef(self):
        """
        method adef(self, func, con) (in decor.mode.Deco_Check)

        Check a condition

        if if_() return True, true_()
        else false_()
        CANNOT MODIFY!

        params:
            $func$: Decorated function
            con: condition

        return:
            $func$
        """

        def adef(func, con="True"):

            setparam = set_param.setparam

            a_11, a_12, wa1 = setparam(self.if_, "d")
            if self.if_(con, *a_12, **a_11):
                a_21, a_22, wa2 = setparam(self.true_, "d")
                self.true_(*a_22, **a_21)
            else:
                a_31, a_32, wa3 = setparam(self.false_, "d")
                self.false_(*a_32, **a_31)
            return func
        return adef


class Deco_Expand(decorator.Deco_iFunction):
    """
    class decor.mode.Deco_Expand(decor.decor.Deco_iFunction)

    Deco_Function 's Expand class

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

                (if not pck, __call__ = decofunc)

        (definition then_do,begin,end)

    self params:
        wrap: (self.begin, decor.FUNCTION, self.end)
        param: global params
        param_it: this params
        pck: is packed

    __str__ -> 'Decorator object: {self.__class__}'
    """
    @property
    def adef(self):
        """
        method adef(self, func) (in decor.mode.Deco_Expand)

        Append 'func' to params

        CANNOT MODIFY!

        params:
            $func$: Decorated function

        return:
            $func$
        """
        def adef(func):
            kwargs, args, wa = set_param.setparam(self, self.then_do, "d")
            if "func" in wa:
                kwargs["func"] = func
                func = self.then_do(*args, **kwargs)
            else:
                self.then_do(*args, **kwargs)
            self._param_it["func"] = func
            return func
        return adef

    def then_do(self):
        """
        method then_do(self) (in decor.mode.Deco_Expand)

        pass
        """
        pass


class Deco_Timer(decorator.Deco_iFunction):
    """
    class decor.mode.Deco_Timer(decor.decor.Deco_iFunction)

    Deco_Function 's Timer Count Class

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

                (if not pck, __call__ = decofunc)

        (definition adef)

    self params:
        wrap: (decor.timecount.time_start, decor.FUNCTION, decor.timecount.time_end)
        param: global params
        param_it: this params
        pck: is packed

    __str__ -> 'Decorator object: {self.__class__}'

    """
    begin = staticmethod(timecount.time_start)
    end = staticmethod(timecount.time_end)
# } function


# {
class Deco_StrOpti(decorator.Deco_iClass):
    """
    class decor.mode.Deco_StrOpti(decor.decor.Deco_iClass)

    A print Optimizer

    method:
        __init__:
            --no params and return--

        __call__:
            params:
                cls: Decorated class

            return:
                cls: New class

        static-add_attr:
            CANNOT MODIFY!
            return:
                funcs: append method list [must be a list]
                attrs: append attribute dict [must be a dict]

    self params:
        method: append method list
        param: append attribute dict(global)
        param_it: append attribute dict(all)
        pck: is packed

    __str__ -> 'Decorator object: {self.__dict__}'
    """
    @staticmethod
    def add_attr():
        """
        static add_attr() (in decor.mode.Deco_StrOpti)

        Add a __str__ in cls

        return:
            funcs: [__str__:
                params:
                    ^self^
                return:
                    res_str: Processing Long Strings
                ]
            attrs: {}
        """
        def __str__(self):
            res_str = "\n"
            line = [f"{self.__class__} object: "]
            for name, value in self.__dict__.items():
                line.append(f"    {name}: {value} ")

            def size(x):
                sum_size = 0
                if isinstance(x, str):
                    a = getsizeof(x)
                    b = getsizeof(x * 5)
                    sum_size = (b-a) // 4
                elif isinstance(x, Iterable):
                    for item in x:
                        sum_size += size(item)
                else:
                    sum_size = getsizeof(x)
                return sum_size

            line.append(f"size: {size(self)}, id: {id(self)}")
            res_str.join(line)
            return res_str
        funcs = [__str__]
        attrs = {}
        return funcs, attrs
# } class
