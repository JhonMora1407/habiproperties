import unittest
from ..querys import Properties


class TestQuerys(unittest.TestCase):

    def test_get(self):
        year = "AND p.year = 2020 "
        city = "AND p.city LIKE '%bogota%' "
        status = "AND s.name LIKE '%pre_venta%' "
        self.assertTrue(Properties().get(year, city, status))
