# -*- coding: utf-8 -*-
import unittest


class TestHandlers(unittest.TestCase):

    def setUp(self):
        from melange import handler
        import copy
        self.original_handler_registry = handler.handler_registry
        handler.handler_registry = copy.deepcopy(handler.handler_registry)

    def tearDown(self):
        from melange import handler
        handler.handler_registry = self.original_handler_registry

    def test_register_first(self):
        from melange.handler import handler_registry

        def testfunc():
            pass  # noqa
        handler_registry.register('foo', testfunc)
        self.assertEqual(handler_registry['foo'], testfunc)

    def test_register_twice(self):
        from melange.handler import handler_registry
        from melange.exceptions import HandlerExistsError

        def testfunc():
            pass  # noqa
        handler_registry.register('foo', testfunc)

        self.assertRaises(
            HandlerExistsError,
            handler_registry.register,
            'foo',
            testfunc,
        )

    def test_register_twice_forced(self):
        from melange.handler import handler_registry

        def testfunc1():
            pass  # noqa

        def testfunc2():
            pass  # noqa
        handler_registry.register('foo', testfunc1)
        handler_registry.register('foo', testfunc2, force=True)
        self.assertEqual(handler_registry['foo'], testfunc2)

    def test_register_decorator(self):
        from melange.handler import melange_handler
        from melange.handler import handler_registry

        @melange_handler('testhandler')
        def testfunc():
            pass  # noqa

        testfunc()
        self.assertEqual(handler_registry['testhandler'], testfunc)
