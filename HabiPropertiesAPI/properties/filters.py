class PropertyFilter:

    def _normalize_integer_filter(self, parameter):
        parameter = int(parameter)

        return parameter

    def _normalize_string_filter(self, parameter):
        parameter = str(parameter)
        parameter = parameter.strip()
        parameter = parameter.lower()

        return parameter

    def filters_has_year(self, filters_year):

        if(filters_year):
            filters_year = self._normalize_integer_filter(filters_year[0])
        
            return """AND p.year = {} """.format(filters_year)
        else:
            return ''

    def filters_has_city(self, filters_city):
        if(filters_city):
            filters_city = self._normalize_string_filter(filters_city[0])

            return """AND p.city LIKE '%{}%' """.format(filters_city)
        else:
            return ''

    def filters_has_status(self, filters_status):
        if(filters_status):
            filters_status = self._normalize_string_filter(filters_status[0])

            return """AND s.name LIKE '%{}%' """.format(filters_status)
        else:
            return ''
