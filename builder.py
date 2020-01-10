class Builder(object):
    def build_body(self):
        raise NotImplementedError()

    def build_battery(self):
        raise NotImplementedError()

    def create_clockhands(self):
        raise NotImplementedError()
        
    def create_clock(self):
        raise NotImplementedError()

class Clock(object):
    """ Настенные часы"""
    def __init__(self, body, battery, clockhands):
        self._body = body
        self._battery = battery
        self.clockhands =clockhands


class Body(object):
    """Корпус"""


class Battery(object):
    """Батарея"""


class ClockHands(object):
    """Стрелки"""


class ClockBuilder(Builder):
    def build_body(self):
        return Body()

    def build_battery(self):
        return Battery()

    def build_clockhands(self):
        return ClockHands()

    def create_clock(self):
        body = self.build_body()
        battery = self.build_battery()
        clockhands = self.build_clockhands()
        return Clock(body, battery, clockhands)


builder = ClockBuilder()
clock = builder.create_clock()
print clock  