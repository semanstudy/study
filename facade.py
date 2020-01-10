class Coce(object):
    """Coca-Cola"""
    def __init__(self, count):
        self._count = count

    def get_count(self):
        return self._count

    def draw(self, text):
        if self._count > 0:
            self._count -= 1
            print text


class VendMach(object):
    """Аппарат с Колой"""
    def error(self, msg):
        print 'Ошибка: %s' % msg

    def vendmach_(self, coce, text):
        if coce.get_count() > 0:
            coce.draw(text)
        else:
            self.error('Напиток закончился')


class Facade(object):
    def __init__(self):
        self._vendmach = VendMach()
        self._coce = Coce(1)

    def write(self, text):
        self._vendmach.vendmach_(self._coce, text)


f = Facade()
f.write('Ваш напиток!') 
f.write('Ваш напиток!') 