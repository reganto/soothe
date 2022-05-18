from tornado.web import Application, RequestHandler, url
from tornado.ioloop import IOLoop
from tornado.options import parse_command_line
from tornado.options import options, define

define("port", default=8000, type=int, help="run on the given port")
define("host", default="0.0.0.0", type=str)


class HelloHandler(RequestHandler):
    def get(self):
        self.write('Hello from Tornado and Docker')


class App(Application):
    def __init__(self):
        handlers = [
            url('/', HelloHandler, name='hello'),
        ]
        settings = dict(
            debug=False,
        )
        super().__init__(handlers, **settings)


if __name__ == '__main__':
    parse_command_line()
    App().listen(options.port, options.host)
    IOLoop.current().start()

