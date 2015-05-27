# -*- coding: utf-8 -*-


class MelangeException(Exception):
    """Melange specific exception
    """


class FragmentError(MelangeException):
    """Fragment is not valid.
    """


class HandlerExistsError(MelangeException):
    """Handler registered twice
    """


class HandlerNotFoundError(MelangeException):
    """Handler not registered
    """


class DynamicLookupError(MelangeException):
    """Handler registered twice
    """
