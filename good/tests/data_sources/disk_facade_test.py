import unittest
from data_sources import disk_facade

from .facade_test_base import FacadeTestBase


class DiskFacadeTest(FacadeTestBase, unittest.TestCase):
    def setUp(self):
        self.facade = disk_facade.DataFacade()
        self.facade.clear()
