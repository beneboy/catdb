import unittest
from data_sources import memory_facade

from .facade_test_base import FacadeTestBase


class MemoryFacadeTest(FacadeTestBase, unittest.TestCase):
    def setUp(self):
        self.facade = memory_facade.DataFacade()
        self.facade.clear()
