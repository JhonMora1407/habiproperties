import unittest
from ..filters import PropertyFilter


class TestFilters(unittest.TestCase):

    def test_filters_has_year(self):
        self.assertTrue(PropertyFilter().filters_has_year(['2021']))
        self.assertTrue(PropertyFilter().filters_has_year([2021]))
        
    def test_filters_has_city(self):
        self.assertTrue(PropertyFilter().filters_has_city(['Bogota']))
        self.assertTrue(PropertyFilter().filters_has_city([' MEDELLIN  ']))
        
    def test_filters_has_status(self):
        self.assertTrue(PropertyFilter().filters_has_status(['en_venta']))
        self.assertTrue(PropertyFilter().filters_has_status(['']))