# -*- coding: utf-8 -*-
from melange.exceptions import HandlerExistsError
from melange.exceptions import HandlerNotFoundError
import UserDict


class HandlerRegistry(UserDict.IterableUserDict):

    def __init__(self):
        self._order = []
        self.data = {}

    def register(self, name, func, force=False, after=None, before=None):
        if not force and name in self._order:
            raise HandlerExistsError(
                'Handler with name {0:s} was already registered.'.format(name)
            )
        self.data[name] = func
        if after is not None:
            idx = self._order.index(after)
            if idx < 0:
                raise HandlerNotFoundError(
                    'Can not insert after {0:s}'.format(after)
                )
            idx += 1
            self._order.insert(idx, name)

        elif before is not None:
            idx = self._order.index(before)
            if idx < 0:
                raise HandlerNotFoundError(
                    'Can not insert before {0:s}'.format(before)
                )
            self._order.insert(idx, name)
        else:
            self._order.append(name)

    def __setitem__(self, key, item):
        self.data[key] = item
        self._order.append(key)

    def keys(self):
        return self._order

    def items(self):
        items = []
        for key in self._order:
            items.append((key, self.data[key]))
            return items

    def iteritems(self):
        for key in self._order:
            yield((key, self.data[key]))

    def iterkeys(self):
        for key in self._order:
            yield key

    def itervalues(self):
        for key in self._order:
            yield(self.data[key])

    def values(self):
        values = []
        for key in self._order:
            values.append(self.data['value'])
        return values

handler_registry = HandlerRegistry()


def melange_handler(name, force=False, after=None, before=None):
    """decorator registers some function as named melange handler
    """
    def wrapper(func):
        handler_registry.register(name, func, force, before, after)
        return func
    return wrapper
