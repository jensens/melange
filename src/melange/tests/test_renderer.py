# -*- coding: utf-8 -*-
import unittest

# testdata
BASE = '''<div data-melange-manifest='{{"name": "testname"}}'>{0:s}</div>'''
MINIMAL = BASE.format('foo')
EXPANDABLE = BASE.format(
    '''<div data-melange-expme='{"name": "expandme"}'>foo</div>'''
)


class TestRenderer(unittest.TestCase):

    def setUp(self):
        from melange import handler
        import copy
        self.original_handler_registry = handler.handler_registry
        handler.handler_registry = copy.copy(handler.handler_registry)

    def tearDown(self):
        from melange import handler
        handler.handler_registry = self.original_handler_registry

    def test_expand_copy(self):
        from melange.fragment import MelangeFragment
        from melange.renderer import expand

        mf = MelangeFragment(MINIMAL)
        mfe = expand(mf, {}, 'view')

        self.assertTrue(mf is not mfe)
        self.assertTrue(mf.html is not mfe.html)

    def test_expand(self):
        from melange.fragment import MelangeFragment
        from melange.handler import melange_handler
        from melange.renderer import expand

        @melange_handler('expme')
        def expme_handler(rt):
            rt['element'].text = 'EXPANDED'

        mf = MelangeFragment(EXPANDABLE)
        mfe = expand(mf, {}, 'view')
        self.assertIn('EXPANDED', str(mfe))
