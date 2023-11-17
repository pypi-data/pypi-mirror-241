from deco import model
import pysnooper


@pysnooper.snoop("./debug.log", depth=1000)
def main():
    class Decorator(model.Deco_Expand):
        def begin(self, func, args, kwargs):
            if func(*args, **kwargs) != (args, kwargs):
                raise TypeError("Cannot modify params")

    @Decorator()
    def modify(*args, **kwargs):
        return kwargs, args

    x, y = modify(1, 2)
    print(x, y)


if __name__ == "__main__":
    main()
