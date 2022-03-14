from servicehandler import ServiceHandler
from http.server import HTTPServer

if __name__ == '__main__':
    server = HTTPServer(('127.0.0.1', 8080), ServiceHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
    server.server_close()
