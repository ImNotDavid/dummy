from unittest import result
import tornado.ioloop
from tornado.web import RequestHandler
import json
from utils import get_printers, get_all_stats, init_printer

printer_list = [init_printer(printer) for printer in get_printers()]

def get_stats():
    global printer_list
    printer_list = get_all_stats(printer_list)
    printers = printer_list
    return printers



class StatsHandler(RequestHandler):

    def get(self):
        stats = get_stats()
        results=[]
        for printer in stats:
            stat = dict(printer)
            del stat['time_update']
            results.append(stat)
        results = json.dumps(results)
        self.write(results)

def make_app():
    return tornado.web.Application([
        (r"/stats", StatsHandler),
    ])

def start_server(port=8888):
    app = make_app()
    app.listen(port)
    print(f'Server started on port {port}')
    tornado.ioloop.IOLoop.current().start()