import unittest
from ..views import PropertyView


class TestPropertyView(unittest.TestCase):
    def test_get(self):
        self.assertTrue(PropertyView(
            ['2020'], ['Bogota'], ['pre_venta']).get())
