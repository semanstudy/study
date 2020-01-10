class AbstractFactory(object):
    def progr_wash(self):
        raise NotImplementedError()

    def progr_capab(self):
        raise NotImplementedError()


class Wash(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Capab(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Factory1(AbstractFactory):
    def progr_wash(self):
        return Wash('AllIncWash')

    def progr_capab(self):
        return Capab('Polish')


class Factory2(AbstractFactory):
    def progr_wash(self):
        return Wash('StandWash')

    def progr_capab(self):
        return Capab('NotInclude')


def get_factory(ident):
    if ident == 0:
        return Factory1()
    elif ident == 1:
        return Factory2()

factory = get_factory(0)
print factory.progr_wash() 
print factory.progr_capab()  