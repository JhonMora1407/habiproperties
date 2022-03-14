from http.server import BaseHTTPRequestHandler
from urllib import parse
from properties.views import PropertyView
import json


class ServiceHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = parse.urlparse(self.path)

        if(parsed_path.path == '/properties'):
            try:
                query = parse.parse_qs(parsed_path.query)

                filter_year = parse.parse_qs(parsed_path.query).get('year')
                filter_city = parse.parse_qs(parsed_path.query).get('city')
                filter_status = parse.parse_qs(parsed_path.query).get('status')

                properties = PropertyView(
                    filter_year, filter_city, filter_status).get()
            except NameError as name_error:
                self.send_error(500, "Something went wrong",
                                name_error.__str__())
            except TypeError as type_error:
                print(type_error.__str__())
                self.send_error(500, "Something went wrong",
                                type_error.__str__())
            except Exception as exception:
                print(exception.__str__)
                self.send_error(500)
            else:
                # defining all the headers
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()

                self.wfile.write(properties)
        else:
            self.send_error(422, 'url not found')
