import datetime
import statistics
from functools import reduce


class History():
    _data = []

    def __init__(self):
        print('pre-init count:', self.count())
        self._data = []
        print('post-init count:', self.count())

    def __str__(self):
        pass

    def append(self, dt: datetime = None, value: float = None) -> str:
        event = self.create_event(dt=dt, value=value)
        self._data.append(event)

    def create_event(self, dt, value):
        return Event(dt, value)

    def count(self):
        return len(self._data)

    def events(self):
        return self._data

    def values(self):
        return [event.value for event in self.events()]

    def max_value(self):
        return reduce(lambda x, y: x if x > y else y, self.values())

    def min_value(self):
        return reduce(lambda x, y: x if x < y else y, self.values())

    def tota(self):
        return self.sum_value()

    def sum_value(self):
        return reduce(lambda x, y: x + y, self.values())

    def average_value(self):
        # return self.sum_value() / self.count()
        return statistics.fmean(self.values())

    def median_value(self):
        # return self.sum_value() / self.count()
        return statistics.median(self.values())

    def mode_value(self):
        # return self.sum_value() / self.count()
        return statistics.mode(self.values())


class Event():
    _dt = None
    _value = None

    def __init__(self, dt, value):
        if not dt:
            dt = datetime.datetime.now()
        elif isinstance(dt, str):
            dt = datetime.datetime.strptime(dt, '%m/%d/%Y %H:%M:%S')
        self._dt = dt
        self._value = value

    @property
    def dt(self):
        return self._dt

    @property
    def value(self):
        return self._value
