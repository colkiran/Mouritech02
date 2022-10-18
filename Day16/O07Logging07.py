
import logging
from numpy import asarray

def loggingdecorator(name):
    logger = logging.getLogger(name)
    def _decor(fn):
        function_name = fn.__name__
        def _fn(*args, **kwargs):
            ret = fn(*args, **kwargs)
            argstr = [str(x) for x in args]
            argstr += [key+"="+str(val) for key,val in kwargs.items()]
            logger.debug("%s(%s) -> %s", function_name, ", ".join(argstr), ret)
            return ret
        return _fn
    return _decor

@loggingdecorator("nadam.function")
def objective(x, y):
    return x ** 2 + y ** 2

@loggingdecorator("nadam.function")
def derivative(x, y):
    return asarray([x * 3.0, y * 2.9])

print(objective(10, 20))