# -*- coding: utf-8 -*-
from melange.exceptions import FragmentError
import json
import lxml.html
import UserDict


class MelangeFragment(object):
    """Single Melange Fragment
    """

    def __init__(self, raw):
        self._manifest = None
        self.raw = raw
        self.html = lxml.html.fromstring(raw)
        self.manifest  # initialize and minor validation

    @property
    def manifest(self):
        """reads manifest from fragment once and caches
        """
        if self._manifest is None:
            for element in self.html.xpath('//*[@data-melange-manifest]'):
                # take first
                raw = element.attrib['data-melange-manifest']
                self._manifest = json.loads(raw)
                break
            if self._manifest is None:
                raise FragmentError('No manifest found.')
            if 'name' not in self._manifest:
                raise FragmentError('Manifest must contain a "name".\n' + raw)
        return self._manifest

    @property
    def name(self):
        return self.manifest['name']

    def __str__(self):
        return lxml.html.tostring(self.html)


class FragmentRegistry(UserDict.IterableUserDict):
    """registry for MelangeFragments
    """

    def register(self, raw):
        fragment = MelangeFragment(raw)
        self.data[fragment.name] = fragment

    def __add__(self, raw):
        self.register(raw)
        return self

fragment_registry = FragmentRegistry()
