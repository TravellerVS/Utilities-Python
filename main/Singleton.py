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
