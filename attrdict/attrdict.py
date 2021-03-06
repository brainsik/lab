# encoding: utf-8
"""
This is yet another dict subclass which enables attribute (i.e., dot notation)
access to items. It differs from other implementations as only valid Python
identifiers and names not matching builtin dict methods or attributes can be
used. This prevents creating items that are only available through index
notation and protects the dict from having expected methods accidentally
demolished.

The goal was to create a dict that could be used as a replacement for Python's
builtin with as little disruption as possible.
"""

class AttrDict(dict):
    """
    A dict subclass which allows attribute (i.e., dot notation) access to
    items. Only valid Python identifiers and names not matching builtin dict
    methods or attributes can be used.
    """

    def __init__(self, *a, **kw):
        dict.__init__(self, *a, **kw)
        for key in self:
            self._validate_key(key)

    def _validate_key(self, key):
        try:
            class IsIdentifier(object): __slots__ = key
        except TypeError:
            raise TypeError("invalid identifier: '%s'" % key)

        try:
            dict.__getattribute__(self, key)
        except AttributeError:
            pass
        else:
            raise TypeError("builtin dict attribute: '%s'" % key)

    def __getattribute__(self, name):
        try:
            return dict.__getattribute__(self, name)
        except AttributeError:
            if name in self:
                return self[name]
            raise

    def __setitem__(self, key, value):
        self._validate_key(key)
        dict.__setitem__(self, key, value)

    __setattr__ = __setitem__

    __delattr__ = dict.__delitem__

    def copy(self, *a, **kw):
        return AttrDict(dict.copy(self, *a, **kw))

    @classmethod
    def fromkeys(cls, *a, **kw):
        return AttrDict(dict.fromkeys(*a, **kw))
