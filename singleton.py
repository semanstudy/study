class SingletonMeta(type):
    def __init__(cls, *args, **kwargs):
        cls._instance = None
        cls.get_instance = classmethod(lambda c: c._instance)
        super(SingletonMeta, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance


class Singleton(object):
    __metaclass__ = SingletonMeta

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


obj1 = Singleton('MyInstance 1')
print obj1.get_name() 

obj2 = Singleton('MyInstance 2')
print obj2.get_name()  

print obj1 is obj2 is Singleton.get_instance()  