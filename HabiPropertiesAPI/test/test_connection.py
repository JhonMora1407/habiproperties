import unittest
from ..connection import Connection


class TestConnection(unittest.TestCase):

    def test_get_queryset(self):
        
        sql = """SELECT p.address, p.city, s.name status, p.price, p.description 
        FROM property p 
        INNER JOIN status_history sh ON p.id = sh.property_id 
        INNER JOIN status s ON sh.status_id = s.id 
        WHERE sh.update_date = (
            SELECT MAX(msh.update_date) 
            FROM status_history msh 
            WHERE msh.property_id = sh.property_id
        )
        GROUP BY sh.property_id"""
        
        self.assertTrue(Connection().get_queryset(sql))