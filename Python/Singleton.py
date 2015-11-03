__author__ = 'Vedran Semenski <vedran.semenski@gmail.com>'



class Singleton(type):
    """
    The Singleton can turn any class into a singleton just my adding it in the __metaclass__.
    This overrides all constructors and returns the original instance of the class.
    example: __metaclass__ = Singleton.Singleton
    This allows easy implementation and removing of singleton characteristics to any class.
    """

    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# **************************************************************
# *********************DEPRICATED SECTION***********************
# **************************************************************

# def singleton(class_):
#       instances = {}
#       def getinstance(*args, **kwargs):
#             if class_ not in instances:
#                 instances[class_] = class_(*args, **kwargs)
#             return instances[class_]
#       return getinstance

# class Singleton:
#     """
#     A non-thread-safe helper class to ease implementing singletons.
#     This should be used as a decorator -- not a metaclass -- to the
#     class that should be a singleton.
#
#     The decorated class can define one `__init__` function that
#     takes only the `self` argument. Other than that, there are
#     no restrictions that apply to the decorated class.
#
#     To get the singleton instance, use the `Instance` method. Trying
#     to use `__call__` will result in a `TypeError` being raised.
#
#     Limitations: The decorated class cannot be inherited from.
#
#     """
#
#     def __init__(self, decorated):
#         self._decorated = decorated
#
#     def Instance(self):
#         """
#         Returns the singleton instance. Upon its first call, it creates a
#         new instance of the decorated class and calls its `__init__` method.
#         On all subsequent calls, the already created instance is returned.
#
#         """
#         try:
#             return self._instance
#         except AttributeError:
#             self._instance = self._decorated()
#             return self._instance
#
#     def __call__(self):
#         raise TypeError('Singletons must be accessed through `Instance()`.')
#
#     def __instancecheck__(self, inst):
#         return isinstance(inst, self._decorated)