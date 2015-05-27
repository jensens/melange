# -*- coding: utf-8 -*-
from melange.exceptions import DynamicLookupError

lookups = []

_marker = dict()


def dynamic_value(rt, identifier):
    """dispatch, first wins
    """
    value = _marker
    for lookup in lookups:
        try:
            value = lookup(rt, identifier)
        except DynamicLookupError:
            continue
    if value is not _marker:
        return value

    # static lookup
    return rt['data'][identifier]
