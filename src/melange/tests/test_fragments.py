# -*- coding: utf-8 -*-
import unittest


class TestFragment(unittest.TestCase):

    def test_initialization_xml_invalid(self):
        from melange.fragment import MelangeFragment
        from melange.exceptions import FragmentError
        self.assertRaises(
            FragmentError,
            MelangeFragment,
            'div'
        )

    def test_initialization_no_manifest(self):
        from melange.fragment import MelangeFragment
        from melange.exceptions import FragmentError
        self.assertRaises(
            FragmentError,
            MelangeFragment,
            '<div></div>',
        )

    def test_initialization_no_name(self):
        from melange.fragment import MelangeFragment
        from melange.exceptions import FragmentError
        self.assertRaises(
            FragmentError,
            MelangeFragment,
            "<div data-melange-manifest='{}'>foo</div>",
        )

    def test_initialization_ok(self):
        from melange.fragment import MelangeFragment
        mf = MelangeFragment(
            '''<div data-melange-manifest='{"name": "testname"}'>foo</div>'''
        )
        self.assertEqual(mf.name, 'testname')

    def test_stringification(self):
        from melange.fragment import MelangeFragment
        raw = '''<div data-melange-manifest='{"name": "testname"}'>foo</div>'''
        mf = MelangeFragment(raw)
        self.assertEqual(str(mf), raw)


class TestFragmentRegistry(unittest.TestCase):

    def test_register(self):
        from melange.fragment import fragment_registry
        raw = '''<div data-melange-manifest='{"name": "testname"}'>foo</div>'''
        fragment_registry += raw
        self.assertIn('testname', fragment_registry)
