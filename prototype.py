import copy

class Prototype(object):
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, attrs):
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attrs)
        return obj

class Cars(object):
    """Марки Авто"""
prototype = Prototype()
prototype.register('cars', Cars())

bmw = prototype.clone('cars', {'name': 'BMW'})
print type(bmw), bmw.name  

nissan = prototype.clone('cars', {'name': 'Nissan'})
print type(nissan), nissan.name  

lada = prototype.clone('cars', {'name': 'Lada'})
print type(lada), lada.name  