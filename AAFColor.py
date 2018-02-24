from collections import namedtuple

X = lambda point: point[0]
Y = lambda point: point[1]
def Z(self):
	return self[2]
'''
Point = namedtuple('Points', ['x', 'y', 'z'], verbose=True)

p = Point(11, 22, 33)

print(Z(p))
print(p.y)

from builtins import property as _property, tuple as _tuple
from operator import itemgetter as _itemgetter
from collections import OrderedDict

class Points(tuple):
    'Points(x, y, z)'

    __slots__ = ()

    _fields = ('x', 'y', 'z')

    def __new__(_cls, x, y, z):
        'Create new instance of Points(x, y, z)'
        return _tuple.__new__(_cls, (x, y, z))

    @classmethod
    def _make(cls, iterable, new=tuple.__new__, len=len):
        'Make a new Points object from a sequence or iterable'
        result = new(cls, iterable)
        if len(result) != 3:
            raise TypeError('Expected 3 arguments, got %d' % len(result))
        return result

    def _replace(_self, **kwds):
        'Return a new Points object replacing specified fields with new values'
        result = _self._make(map(kwds.pop, ('x', 'y', 'z'), _self))
        if kwds:
            raise ValueError('Got unexpected field names: %r' % list(kwds))
        return result

    def __repr__(self):
        'Return a nicely formatted representation string'
        return self.__class__.__name__ + '(x=%r, y=%r, z=%r)' % self

    def _asdict(self):
        'Return a new OrderedDict which maps field names to their values.'
        return OrderedDict(zip(self._fields, self))

    def __getnewargs__(self):
        'Return self as a plain tuple.  Used by copy and pickle.'
        return tuple(self)

    x = _property(_itemgetter(0), doc='Alias for field number 0')

    y = _property(_itemgetter(1), doc='Alias for field number 1')

    z = _property(_itemgetter(2), doc='Alias for field number 2')


33
22

'''