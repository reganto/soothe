from tornado.web import Application, RequestHandler, url
from tornado.ioloop import IOLoop
from tornado.options import parse_command_line, define, options
from tornado.websocket import WebSocketHandler


define(
    "port",
    default=8000,
    type=int,
    help="run on the given port",
)


class HomeHandler(RequestHandler):
    def get(self):
        self.render("index.html")


class BaseConnection(WebSocketHandler):
    def send(self, participant, message):
        participant.write_message(message)

    def broadcast(self, participants, message):
        for participant in participants:
            self.send(participant, message)


class ChatConnection(BaseConnection):
    participants = set()

    def open(self):
        self.broadcast(
            self.participants,
            "Someone joined to room",
        )
        self.participants.add(self)

    def on_message(self, message):
        self.broadcast(
            self.participants,
            message,
        )

    def on_close(self):
        self.participants.remove(self)
        self.broadcast(
            self.participants,
            "Someone leaved room",
        )


class App(Application):
    def __init__(self):
        handlers = [
            url("/", HomeHandler, name="foo"),
            url("/ws", ChatConnection, name="chat"),
        ]
        settings = dict(
            debug=True,
        )
        super().__init__(handlers, **settings)


if __name__ == "__main__":
    parse_command_line()
    App().listen(options.port)
    IOLoop.current().start()
