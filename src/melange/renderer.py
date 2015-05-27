# -*- coding: utf-8 -*-
from melange.exceptions import FragmentError
from melange.handler import handler_registry
import copy
import json
import lxml.etree

XPATH_MELANGE_DATA = "@*[starts-with(name(), 'data-melange-{0:s}')]"


def _iter_html(element):
    yield element
    for child in element.getchildren():
        for sub in _iter_html(child):
            yield sub


def expand(fragment, data, mode, context=None):
    """Expand the fragment using the given data and parameters

    This creates a new expanded fragment.

    :param fragment: [required] fragment to be expanded
    :type fragment: MelangeFragment object
    :param data: [required] data with data to be used for rendering
    :type dict: dict-like object
    :param mode: [required] a mode to be considered by handler
    :type string: a string ``view`` or ``edit``
    :param context: some context, depends on the framework
    :type dict: a dictionary with context related objects
    :rtype: MelangeFragment
    """
    scopes = []
    runtime = {}
    runtime['fragment'] = copy.deepcopy(fragment)
    runtime['data'] = copy.deepcopy(data)
    runtime['mode'] = mode
    runtime['context'] = context
    runtime['scope'] = {}
    for action, element in lxml.etree.iterwalk(
        runtime['fragment'].html,
        events=('start', 'end')
    ):
        if action == 'end':
            runtime['scope'] = scopes.pop()
            continue
        scopes.append(runtime['scope'])
        runtime['scope'] = copy.deepcopy(runtime['scope'])
        for name in handler_registry:
            expression = XPATH_MELANGE_DATA.format(name)
            declarations = element.xpath(expression)
            if not declarations:
                continue
            if len(declarations) > 1:
                raise FragmentError(
                    'Declaration for {0:s} multiple times on same tag.'.format(
                        name
                    )
                )
            runtime['handlername'] = name
            runtime['declaration'] = json.loads(declarations[0])
            runtime['element'] = element
            handler_registry[name](runtime)
    return runtime['fragment']


def render(fragment, data, mode, context=None):
    """Render the fragment after exanping it using given data and parameters

    This creates a text-rendered expanded fragment.

    :param fragment: [required] fragment to be expanded
    :type fragment: MelangeFragment object
    :param data: [required] data with data to be used for rendering
    :type dict: dict-like object
    :param mode: [required] a mode to be considered by handler
    :type string: a string ``view`` or ``edit``
    :param context: some context, depends on the framework
    :type dict: a dictionary with context related objects
    :returns: fragment rendered as text.
    :rtype: string
    """
    expanded_fragment = expand(fragment, data, mode, context=None)
    return str(expanded_fragment)
