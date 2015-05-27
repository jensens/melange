# -*- coding: utf-8 -*-
from melange.dynamic import dynamic_value
from melange.handler import melange_handler
import copy
import json

MODE_VIEW = 'view'
MODE_EDIT = 'edit'


def _remove_data_attr(rt, modes=(MODE_VIEW,)):
    if rt['mode'] not in modes:
        return
    del rt['element'].attrib['data-melange-{0:s}'.format(rt['handlername'])]


@melange_handler('manifest')
def manifest(rt):
    _remove_data_attr(rt)


@melange_handler('content')
def content(rt):
    # render content
    _remove_data_attr(rt)
    rt['element'].text = dynamic_value(rt, rt['declaration']['name'])


@melange_handler('attrs')
def attributes(rt):
    # render attributes
    _remove_data_attr(rt)
    for field in rt['declaration']:
        rt['element'].attrib[field['name']] = dynamic_value(rt, field['field'])


@melange_handler('loop')
def loop(rt):
    # render attributes
    _remove_data_attr(rt)
    values = dynamic_value(rt, rt['declaration']['name'])
    length = len(values)
    children = rt['element'].getchildren()
    for child in children:
        rt['element'].remove(child)
    for idx, value in enumerate(values):
        loop_data = {
            'data': value,
            'index': idx,
            'length': length,
            'even': not bool(idx % 2),
            'odd': bool(idx % 2),
            'first': idx == 0,
            'last': idx == len(values) - 1
        }
        for child in children:
            new_child = copy.deepcopy(child)
            new_child.attrib['scope'] = json.dumps([
                {
                    'method': 'stack',
                    'data': {'loops': loop_data},
                }
            ])
            rt['element'].append(new_child)


@melange_handler('scope')
def scope(rt):
    _remove_data_attr(rt)
    if 'stack' in rt['declaration']:
        for key, value in rt['declaration']['stack'].items():
            if key not in rt['scope']:
                rt['scope'][key] = []
            rt['scope'][key].append(value)
    if 'update' in rt['declaration']:
        rt['scope'].update(rt['declaration']['update'])


@melange_handler('nested')
def nested(rt):
    _remove_data_attr(rt)
    # TODO
