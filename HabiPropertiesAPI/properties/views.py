from .querys import Properties
from .filters import PropertyFilter
import json


class PropertyView:

    def __init__(self, filter_year, filter_city, filter_status):
        self._year = PropertyFilter().filters_has_year(filter_year)
        self._city = PropertyFilter().filters_has_city(filter_city)
        self._status = PropertyFilter().filters_has_status(filter_status)

    def get(self):

        property = []
        fields_names, data = Properties().get(self._year, self._city, self._status)
        fields_names = [col[0] for col in fields_names]

        for datium in data:

            property.append({
                fields_names[0]: datium[0],
                fields_names[1]: datium[1],
                fields_names[2]: datium[2],
                fields_names[3]: datium[3],
                fields_names[4]: datium[4]
            })

        return json.dumps(property).encode()
