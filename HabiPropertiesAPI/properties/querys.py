from ..connection import Connection
from .utils import property_status


class Properties(Connection):

    def get(self, year, city, status):

        sql = """SELECT p.address, p.city, s.name status, p.price, p.description 
        FROM property p 
        INNER JOIN status_history sh ON p.id = sh.property_id 
        INNER JOIN status s ON sh.status_id = s.id 
        WHERE s.name in ('{0}', '{1}', '{2}')
        AND sh.update_date = (
            SELECT MAX(msh.update_date) 
            FROM status_history msh 
            WHERE msh.property_id = sh.property_id
        )
        {3}{4}{5} 
        GROUP BY sh.property_id""".format(property_status['3'], property_status['4'], property_status['5'], year, city, status)

        return self.get_queryset(sql)
